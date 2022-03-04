import asyncio
from typing import List, Union

import grpc
import structlog
from click import ClickException
from meltano.core.block.blockset import BlockSet, BlockSetValidationError
from meltano.core.block.parser import BlockParser, validate_block_sets
from meltano.core.block.plugin_command import PluginCommandBlock
from meltano.core.job import JobFinder
from meltano.core.logging import OutputLogger, setup_logging
from meltano.core.project import Project
from meltano.core.runner import RunnerError
from structlog import BoundLogger

import run_pb2 as pb2
import run_pb2_grpc as pb2_grpc

logger = structlog.getLogger(__name__)


async def _run_blocks(
    log: BoundLogger,
    parsed_blocks: List[Union[BlockSet, PluginCommandBlock]],
    project: Project,
) -> None:

    job_results = []
    for idx, blk in enumerate(parsed_blocks):
        job_id = f"{project.active_environment.name}:{blk.head.string_id}-to-{blk.tail.string_id}"
        finder = JobFinder(job_id)

        try:
            await blk.run()
        except RunnerError as err:
            log.error(
                "Block run completed.",
                set_number=idx,
                block_type=blk.__class__.__name__,
                success=False,
                err=err,
                exit_codes=err.exitcodes,
            )
            raise Exception(
                f"Run invocation could not be completed as block failed: {err}"
            ) from err
        log.info(
            "Block run completed.",
            set_number=idx,
            block_type=blk.__class__.__name__,
            success=True,
            err=None,
        )
        last = finder.latest(blk.context.session)
        job_results.append(
            pb2.Job(
                id=last.id,
                job_id=last.job_id,
                state=str(last.state),
            )
        )
    result = pb2.Result()
    result.jobs.extend(job_results)
    return result


def trace_id(context: grpc.aio.ServicerContext) -> str:
    for k, v in context.invocation_metadata():
        if k == "x-meltano-trace-id":
            return v
    return "no-trace-id"


class RunService(pb2_grpc.RunServicer):
    def __init__(self, project: Project):
        self.project = project
        logger.info(
            "Found project",
            project=self.project,
            meltano_dir=self.project.meltano_dir(),
            environment=self.project.active_environment.name,
        )

    async def Submit(
        self, request: pb2.Command, context: grpc.aio.ServicerContext
    ) -> pb2.Result:
        log = logger.bind(trace_id=trace_id(context))

        log.info("Received command", cmd=request)
        blocks = request.blocks.split(" ")
        try:
            parser = BlockParser(
                logger, self.project, blocks, request.full_refresh, False, request.force
            )
        except ClickException as e:
            log.error(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return pb2.Result()

        try:
            parsed_blocks = list(parser.find_blocks(0))
        except BlockSetValidationError as e:
            log.error(e)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return pb2.Result()

        if validate_block_sets(log, parsed_blocks):
            log.debug("All ExtractLoadBlocks validated, starting execution.")
            results = await _run_blocks(log, parsed_blocks, self.project)
            log.warning("done")
            return results
        else:
            log.error("Validation failed.")
            context.set_details("Validation failed.")
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            return pb2.Result()


async def serve(project) -> None:
    server = grpc.aio.server()

    pb2_grpc.add_RunServicer_to_server(RunService(project), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logger.debug("Starting server", listen_addr=listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    project = Project.find()
    project.activate_environment("dev")
    setup_logging(project, log_level="INFO")
    asyncio.run(serve(project))

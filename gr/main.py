import asyncio
import logging
from concurrent import futures
from typing import List, Union

import grpc
import structlog
from click import ClickException
from meltano.core.block.blockset import BlockSet, BlockSetValidationError
from meltano.core.block.parser import BlockParser, validate_block_sets
from meltano.core.block.plugin_command import PluginCommandBlock
from meltano.core.logging import setup_logging
from meltano.core.project import Project
from meltano.core.project_settings_service import ProjectSettingsService
from meltano.core.runner import RunnerError
from structlog import BoundLogger
from structlog.contextvars import bind_contextvars, clear_contextvars

import run_pb2 as pb2
import run_pb2_grpc as pb2_grpc

logger = structlog.getLogger(__name__)


async def _run_blocks(
    log: BoundLogger, parsed_blocks: List[Union[BlockSet, PluginCommandBlock]]
) -> None:
    for idx, blk in enumerate(parsed_blocks):
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


def trace_id(context: grpc.aio.ServicerContext) -> str:
    for k, v in context.invocation_metadata():
        if k == "x-meltano-trace-id":
            return v
    return "no-trace-id"


class RunService(pb2_grpc.RunServicer):
    def __init__(self):
        self.project = Project.find()
        logger.info(
            "Found project",
            project=self.project,
            meltano_dir=self.project.meltano_dir(),
        )

    async def Submit(
        self, request: pb2.Command, context: grpc.aio.ServicerContext
    ) -> pb2.MessageResponse:
        log = logger.bind(trace_id=trace_id(context))

        log.info("Received command", cmd=request.message)
        blocks = request.message.split(" ")
        try:
            parser = BlockParser(logger, self.project, blocks, False, True, False)
        except ClickException as e:
            log.error(e)
            return pb2.MessageResponse(message=str(e), submitted=False)

        try:
            parsed_blocks = list(parser.find_blocks(0))
        except BlockSetValidationError as e:
            log.error(e)
            return pb2.MessageResponse(message=str(e), submitted=False)

        if not parsed_blocks:
            log.info("No valid blocks found.")
            return pb2.MessageResponse(
                message=f"No valid blocks found.",
                submitted=False,
            )
        if validate_block_sets(log, parsed_blocks):
            log.debug("All ExtractLoadBlocks validated, starting execution.")
            await _run_blocks(log, parsed_blocks)
            return pb2.MessageResponse(
                message=f"All ExtractLoadBlocks validated, starting execution.",
                submitted=True,
            )


async def serve() -> None:
    server = grpc.aio.server()

    pb2_grpc.add_RunServicer_to_server(RunService(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logger.info("Starting server", listen_addr=listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    setup_logging()
    asyncio.run(serve())

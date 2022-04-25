from typing import List, Optional, Union

import structlog
from click import ClickException
from fastapi import APIRouter, Depends, HTTPException, status
from meltano.core.block.blockset import BlockSet, BlockSetValidationError
from meltano.core.block.parser import BlockParser, validate_block_sets
from meltano.core.block.plugin_command import PluginCommandBlock
from meltano.core.job import JobFinder
from meltano.core.logging import setup_logging
from meltano.core.project import Project
from meltano.core.runner import RunnerError
from pydantic import BaseModel, Field
from structlog import BoundLogger

from ..dependencies import get_env, get_trace_id
from ..settings import settings

logger = structlog.getLogger(__name__)


router = APIRouter(
    prefix="/run",
    tags=["run"],
    dependencies=[Depends(get_trace_id), Depends(get_env)],
    responses={404: {"description": "Not found"}},
)


class SubmitRequest(BaseModel):
    blocks: str = Field(
        ..., description="The blocks to run", example="tap-gitlab target-jsonl"
    )
    full_refresh: bool = Field(False, description="Whether to perform a full refresh")
    force: bool = Field(
        False,
        description="Whether to force a run even if a job with the same ID is already running",
    )


class Job(BaseModel):
    id: int
    job_id: str
    state: str

    class Config:
        schema_extra = {
            "example": {
                "id": 42,
                "job_id": "dev:tap-gitlab-to-target-jsonl",
                "state": "SUCCESS",
            }
        }


class SubmitResponse(BaseModel):
    """Class level comments on models also get spit out in the schema and rendered in openapi docs."""

    jobs: Optional[List[Job]] = None


async def _run_blocks(
    log: BoundLogger,
    parsed_blocks: List[Union[BlockSet, PluginCommandBlock]],
    project: Project,
) -> SubmitResponse:

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
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "message": "Run invocation could not be completed as block failed.",
                    "error": err,
                },
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
            Job(
                id=last.id,
                job_id=last.job_id,
                state=str(last.state),
            )
        )
    result = SubmitResponse()
    result.jobs = job_results
    return result


@router.get("/", tags=["just-a-test"])
async def get_run():
    return {"message": "thanks for asking, but you can't GET this"}


@router.post("/", tags=["just-a-test"], response_model=SubmitResponse)
async def submit_run(request: SubmitRequest):
    log = logger.bind(thing="thing")
    log.info("Received command", cmd=request)
    settings.project.activate_environment("dev")
    setup_logging(settings.project, log_level="INFO")

    blocks = request.blocks.split(" ")
    try:
        parser = BlockParser(
            logger, settings.project, blocks, request.full_refresh, False, request.force
        )
    except ClickException as err:
        log.error(err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Run invocation could not be completed as parsing of blocks failed.",
                "error": err.message,
            },
        ) from err

    try:
        parsed_blocks = list(parser.find_blocks(0))
    except BlockSetValidationError as err:
        log.error(err)
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail={
                "message": "Block set validation failed.",
                "error": str(err),
            },
        ) from err

    if validate_block_sets(log, parsed_blocks):
        log.debug("All ExtractLoadBlocks validated, starting execution.")
        results = await _run_blocks(log, parsed_blocks, settings.project)
        return results
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "Block set validation failed."},
        )

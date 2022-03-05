"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SubmitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BLOCKS_FIELD_NUMBER: builtins.int
    FULL_REFRESH_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    blocks: typing.Text
    full_refresh: builtins.bool
    force: builtins.bool
    def __init__(self,
        *,
        blocks: typing.Text = ...,
        full_refresh: builtins.bool = ...,
        force: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["blocks",b"blocks","force",b"force","full_refresh",b"full_refresh"]) -> None: ...
global___SubmitRequest = SubmitRequest

class SubmitResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    JOBS_FIELD_NUMBER: builtins.int
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Job]: ...
    def __init__(self,
        *,
        jobs: typing.Optional[typing.Iterable[global___Job]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jobs",b"jobs"]) -> None: ...
global___SubmitResponse = SubmitResponse

class Job(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    id: builtins.int
    job_id: typing.Text
    state: typing.Text
    def __init__(self,
        *,
        id: builtins.int = ...,
        job_id: typing.Text = ...,
        state: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","job_id",b"job_id","state",b"state"]) -> None: ...
global___Job = Job

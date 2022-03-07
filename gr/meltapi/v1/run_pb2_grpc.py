# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from meltapi.v1 import run_pb2 as meltapi_dot_v1_dot_run__pb2


class RunServiceStub(object):
    """RunService provides a way to execute a `meltano run` like command via GRPC.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Submit = channel.unary_unary(
                '/meltapi.v1.RunService/Submit',
                request_serializer=meltapi_dot_v1_dot_run__pb2.SubmitRequest.SerializeToString,
                response_deserializer=meltapi_dot_v1_dot_run__pb2.SubmitResponse.FromString,
                )


class RunServiceServicer(object):
    """RunService provides a way to execute a `meltano run` like command via GRPC.
    """

    def Submit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RunServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Submit': grpc.unary_unary_rpc_method_handler(
                    servicer.Submit,
                    request_deserializer=meltapi_dot_v1_dot_run__pb2.SubmitRequest.FromString,
                    response_serializer=meltapi_dot_v1_dot_run__pb2.SubmitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'meltapi.v1.RunService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RunService(object):
    """RunService provides a way to execute a `meltano run` like command via GRPC.
    """

    @staticmethod
    def Submit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meltapi.v1.RunService/Submit',
            meltapi_dot_v1_dot_run__pb2.SubmitRequest.SerializeToString,
            meltapi_dot_v1_dot_run__pb2.SubmitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

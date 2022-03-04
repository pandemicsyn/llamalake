import asyncio
import logging

import grpc
from concurrent import futures
import run_pb2_grpc as pb2_grpc
import run_pb2 as pb2


class RunService(pb2_grpc.RunServicer):

    async def Submit(self, request: pb2.Command, context: grpc.aio.ServicerContext) -> pb2.MessageResponse:
        return pb2.MessageResponse(
            message='would execute' % request.message,
            received=True,
        )


async def serve() -> None:
    server = grpc.aio.server()

    pb2_grpc.add_RunServicer_to_server(RunService(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
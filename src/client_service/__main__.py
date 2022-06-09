import asyncio
import client_service.factories as factories
import generated.kaif_client_service_pb2_grpc as pb2_grpc
import grpc


async def serve() -> None:
    server = grpc.aio.server()
    pb2_grpc.add_ClientServiceServicer_to_server(
        factories.get_client_service(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


def run() -> None:
    asyncio.get_event_loop().run_until_complete(serve())


if __name__ == '__main__':
    run()


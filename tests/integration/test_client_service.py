from google.protobuf.empty_pb2 import Empty
import generated.kaif_client_service_pb2 as pb2
import client_service.domain.dtos as dtos
import client_service.web.mappers as mappers

from sqlalchemy.ext.asyncio.session import AsyncSession


async def test_add_client(client_service_stub, session: AsyncSession):
    client = pb2.Client(telegram_id=123, telegram_username="test_username",
                        telegram_fullname="test_fullname")

    try:
        client_service_stub.AddClient(client)

        client_dto = await session.get(dtos.Client, client.telegram_id)
        assert client_dto == mappers.client_grpc_to_dto(client)

    finally:
        client_dto = await session.get(dtos.Client, client.telegram_id)
        await session.delete(client_dto)
        await session.commit()
    

async def test_get_client(client_service_stub, session: AsyncSession):
    client = pb2.Client(telegram_id=123, telegram_username="test_username",
                        telegram_fullname="test_fullname")

    try:
        client_service_stub.AddClient(client)
        request = pb2.ClientRequest(telegram_id=client.telegram_id)
        new_client = client_service_stub.GetClient(request)

        assert new_client == client

    finally:
        client_dto = await session.get(dtos.Client, client.telegram_id)
        await session.delete(client_dto)
        await session.commit()


async def test_get_all_clients(client_service_stub, session: AsyncSession):
    clients = [
        pb2.Client(telegram_id=i, telegram_username="test_username",
                        telegram_fullname="test_fullname")
        for i in range(10)
    ]

    try:
        for client in clients:
            client_service_stub.AddClient(client)

        new_clients = [c for c in client_service_stub.GetAllClients(Empty())]

        before_ids = [c.telegram_id for c in clients]
        after_ids = [c.telegram_id for c in new_clients]

        assert before_ids == after_ids

    finally:
        for client in clients:
            client_dto = await session.get(dtos.Client, client.telegram_id)
            await session.delete(client_dto)

        await session.commit()


async def test_update_client(client_service_stub, session: AsyncSession):
    client = pb2.Client(telegram_id=123, telegram_username="test_username",
                        telegram_fullname="test_fullname")

    updated_client = pb2.Client(telegram_id=123, telegram_username="other",
                                telegram_fullname="other")

    try:
        client_service_stub.AddClient(client)
        client_service_stub.UpdateClient(updated_client)
        new_client = client_service_stub.GetClient(updated_client)

        assert new_client == updated_client
    finally:
        client_dto = await session.get(dtos.Client, client.telegram_id)
        await session.delete(client_dto)
        await session.commit()


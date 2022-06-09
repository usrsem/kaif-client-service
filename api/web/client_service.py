from typing import Optional
import api.domain.dtos as dtos
from api.repository.repository_uow import RepositoryUow
from generated.kaif_client_service_pb2 import Client, ClientRequest, ClientsList
from generated.kaif_client_service_pb2_grpc import ClientService


class ClientsService(ClientService):

    def __init__(self, uow: RepositoryUow) -> None:
        self.uow: RepositoryUow = uow

    async def AddClient(self, client: Client) -> None:
        client_dto: dtos.Client = mappers.client_grpc_to_dto(client)

        async with self.uow:
            await self.uow.clients.add(client_dto)
            await self.uow.commit()

    async def GetClient(self, request: ClientRequest) -> Client:
        async with self.uow:
            client_dto = await self.uow.clients.find_by_telegram_id(
                    request.telegram_id)
            await self.uow.commit()

        if client_dto is not None:
            return mappers.client_dto_to_grpc(client_dto)

    async def GetAllClients(self) -> ClientsList:
        async with self.uow:
            clients = await self.uow.clients.get_all()
            await self.uow.commit()

        return ClientsList(clients=clients)

    async def UpdateClient(self, client: Client) -> None:
        client_dto = mappers.client_grpc_to_dto(client)

        async with self.uow:
            await self.uow.clients.update(client_dto)
            await self.uow.commit()



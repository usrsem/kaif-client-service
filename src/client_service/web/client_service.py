from typing import AsyncGenerator
from google.protobuf.empty_pb2 import Empty
import client_service.domain.dtos as dtos
import client_service.web.mappers as mappers 
import generated.kaif_client_service_pb2_grpc as pb2

from client_service.repository.repository_uow import RepositoryUow
from client_service.loader import log
from generated.kaif_client_service_pb2 import Client, ClientRequest


class V1ClientService(pb2.ClientService):

    def __init__(self, uow: RepositoryUow) -> None:
        self.uow: RepositoryUow = uow

    async def AddClient(self, client: Client, _) -> Empty:
        log.debug(f"Adding client {client}")
        client_dto: dtos.Client = mappers.client_grpc_to_dto(client)

        async with self.uow:
            await self.uow.clients.add(client_dto)
            await self.uow.commit()

        return Empty()

    async def GetClient(self, request: ClientRequest, _) -> Client:
        log.debug(f"Getting client {request}")
        async with self.uow:
            client_dto = await self.uow.clients.find_by_telegram_id(
                    request.telegram_id)
            await self.uow.commit()

        if client_dto is not None:
            return mappers.client_dto_to_grpc(client_dto)

        raise Exception(f"Client with id: {request.telegram_id} "
                        "not found in db")

    async def GetAllClients(self, *_) -> AsyncGenerator[Client, None]:
        log.debug(f"Getting all clients")

        async with self.uow:
            clients_dtos = await self.uow.clients.get_all()
            await self.uow.commit()

        for client in clients_dtos:
            log.debug(f"Sending client: {client}")
            yield mappers.client_dto_to_grpc(client)

    async def UpdateClient(self, client: Client, _) -> Empty:
        log.debug(f"Updating client {client}")
        client_dto = mappers.client_grpc_to_dto(client)

        async with self.uow:
            await self.uow.clients.update(client_dto)
            await self.uow.commit()

        return Empty()


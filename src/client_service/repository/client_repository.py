import dataclasses

from client_service.domain.dtos import Client
from typing import Optional, Protocol
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from sqlalchemy.future import select


class ClientRepository(Protocol):
    async def add(self, client: Client) -> None: ...
    async def find_by_telegram_id(self, id: int) -> Optional[Client]: ...
    async def get_all(self) -> list[Client]: ...
    async def update(self, client: Client) -> None: ...


class SqlAclhemyClientRepository:
    async def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def add(self, client: Client) -> None:
        self._session.add(client)

    async def find_by_telegram_id(self, id: int) -> Optional[Client]:
        return (await self._session.execute(
             select(Client)
             .where(Client.telegram_id == id)
             .scalars()
             .first()))

    async def get_all(self) -> list[Client]:
        result = await self._session.execute(select(Client))
        return result.scalars().all()

    async def update(self, client: Client) -> None:
        q = (update(Client)
            .where(Client.telegram_id == client.telegram_id)
            .values(**dataclasses.asdict(client)))

        await self._session.execute(q)


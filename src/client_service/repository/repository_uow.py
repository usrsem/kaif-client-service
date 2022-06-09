from typing import Protocol

from sqlalchemy.ext.asyncio.session import AsyncSession

from client_service.repository.client_repository import ClientRepository, SqlAclhemyClientRepository


class RepositoryUow(Protocol):
    clients: ClientRepository

    async def __aenter__(self) -> None: ...
    async def __aexit__(self, *args) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...


class SqlAlchemyRepositoryUow:
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session
        self.clients: ClientRepository

    async def __aenter__(self) -> None:
        self.clients = SqlAclhemyClientRepository(self._session)

    async def __aexit__(self, *args) -> None:
        await self.rollback()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()


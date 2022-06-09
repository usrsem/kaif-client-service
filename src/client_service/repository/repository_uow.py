from typing import Protocol
from sqlalchemy.ext.asyncio.engine import create_async_engine

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import sessionmaker

from client_service.repository.client_repository import ClientRepository, SqlAclhemyClientRepository


class RepositoryUow(Protocol):
    clients: ClientRepository

    async def __aenter__(self) -> None: ...
    async def __aexit__(self, *args) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...


class SqlAlchemyRepositoryUow:
    def __init__(self, pg_url: str) -> None:
        self._pg_url = pg_url
        self.clients: ClientRepository

    async def __aenter__(self) -> None:
        self.engine = create_async_engine(self._pg_url)

        async_session = sessionmaker(
                self.engine, expire_on_commit=False, class_=AsyncSession)

        self._session = async_session()
        self.clients = SqlAclhemyClientRepository(self._session)

    async def __aexit__(self, *args) -> None:
        await self.rollback()
        await self.engine.dispose()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()


import pytest
import grpc
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import sessionmaker
from client_service.loader import DEFAULT_SESSION_FACTORY
from client_service.repository.repository_uow import SqlAlchemyRepositoryUow
from config import ASYNC_PG_URL
import generated.kaif_client_service_pb2_grpc as pb2_grpc


@pytest.fixture
async def session():
    engine = create_async_engine(ASYNC_PG_URL)
    async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        yield session

    await engine.dispose()


@pytest.fixture(scope="function")
def client_service_stub():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.ClientServiceStub(channel)
        yield stub


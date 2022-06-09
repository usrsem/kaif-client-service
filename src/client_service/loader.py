from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import sessionmaker
from config import ASYNC_PG_URL
from db.mappers import start_mappers, get_query_cls
from loguru import logger


log = logger

log.info("Loader started")

start_mappers()

DEFAULT_SESSION_FACTORY = sessionmaker(
    create_async_engine(ASYNC_PG_URL, echo=True),
    query_cls=get_query_cls,
    expire_on_commit=False,
    class_=AsyncSession)


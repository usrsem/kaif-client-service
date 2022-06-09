import os
from pydantic import BaseSettings

prefix: str = "KAIF_CLIENT_SERVICE_"

class Settings(BaseSettings):
    pg_host: str = os.getenv(prefix + "PG_HOST", "localhost:49153")
    pg_user: str = os.getenv(prefix + "PG_USER", "postgres")
    pg_password: str = os.getenv(prefix + "PG_PASSWORD", "postgrespw")
    pg_db_name: str = os.getenv(prefix + "PG_DB_NAME", "client")


settings = Settings()


SYNC_PG_URL = (
    f"postgresql://{settings.pg_user}:{settings.pg_password}"
    f"@{settings.pg_host}/{settings.pg_db_name}")

ASYNC_PG_URL = (
    f"postgresql+asyncpg://{settings.pg_user}:{settings.pg_password}"
    f"@{settings.pg_host}/{settings.pg_db_name}")


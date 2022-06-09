from sqlalchemy.engine.create import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

from config import SYNC_PG_URL


engine = create_engine(SYNC_PG_URL)
metadata = MetaData(bind=engine)


client_table = Table(
    'client',
    metadata,
    Column('telegram_id', Integer, primary_key=True),
    Column('telegram_username', String, nullable=True, index=True),
    Column('telegram_fullname', String, nullable=False),
)


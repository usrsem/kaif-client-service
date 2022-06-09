from db.schemas import client_table
from sqlalchemy.orm import mapper
from sqlalchemy.orm import Mapper, Query
from client_service.domain.dtos import Client

def start_mappers():
    mapper(Client, client_table)


def get_query_cls(mapper, session):
    if mapper:
        m = mapper
        if isinstance(m, tuple):
            m = mapper[0]
        if isinstance(m, Mapper):
            m = m.entity

        try:
            return m.__query_cls__(mapper, session)
        except AttributeError:
            pass

    return Query(mapper, session)


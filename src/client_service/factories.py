from client_service.loader import DEFAULT_SESSION_FACTORY
from client_service.repository.repository_uow import RepositoryUow, SqlAlchemyRepositoryUow
from client_service.web.client_service import V1ClientService


def get_repository_uow() -> RepositoryUow:
    return SqlAlchemyRepositoryUow(DEFAULT_SESSION_FACTORY())


def get_client_service() -> V1ClientService:
    return V1ClientService(get_repository_uow())


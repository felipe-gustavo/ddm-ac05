import inject

from src.main.contracts.user_repository_contract import UserRepositoryContract
from src.shared.infra.persistence.sqlalchemy.repositories.user_repository import UserRepository


def config(binder: inject.Binder):
    binder.bind(UserRepositoryContract, UserRepository)


inject.configure(config)

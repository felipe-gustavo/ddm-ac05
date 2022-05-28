import inject

from main.contracts.user_repository_contract import UserRepositoryContract
from src.main.value_objects.user_value_object import User
from ..orm.entities.user_model import User as UserModel
from ..connection import Session


class UserRepository(UserRepositoryContract):
    session = inject.attr(Session)

    def create(self, user: User) -> User:
        values = dict(
            name=user.name,
            email=user.name,
            password=user.meta['password']
        )
        self.session.execute(
            UserModel.__table__.insert(),
            values
        )
        self.session.commit()

from abc import ABC, abstractmethod
from src.main.value_objects.user_value_object import User


class UserRepositoryContract(ABC):
    @abstractmethod
    def create(user: User) -> User:
        pass

import inject
from src.main.contracts.user_repository_contract import UserRepositoryContract
from src.main.value_objects.user_value_object import User


class HostessWorker:
    userRepository = inject.attr(UserRepositoryContract)

    def registerUser(self, user: User):
        self.userRepository.create(user)

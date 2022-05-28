import inject

from src.main.workers.hostess.hostess_worker import HostessWorker


class SignupUseCase:
    hostessWorker = inject.attr(HostessWorker)

    def signUp():
        pass

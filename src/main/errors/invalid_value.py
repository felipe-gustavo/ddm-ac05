from .main_error import MainError


class InvalidValue(MainError):
    def __init__(self, message) -> None:
        super().__init__(message)

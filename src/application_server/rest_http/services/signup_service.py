import inject

from application_server.use_case.sign_up_use_case import SignupUseCase


class SignupService:
    signupUseCase = inject.attr(SignupUseCase)

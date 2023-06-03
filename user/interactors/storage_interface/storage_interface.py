import abc

from user.interactors.dtos import RegisterUserDetailsDTO
from user.models import User


class StorageInterface:

    @abc.abstractmethod
    def register_user(self, register_user_details_dto: RegisterUserDetailsDTO) -> int:
        pass

    @abc.abstractmethod
    def check_is_user_already_registered(self, email: str) -> User:
        pass

    @abc.abstractmethod
    def get_user_phone_number(self, email: str):
        pass

    @abc.abstractmethod
    def create_user_otp(self, user_id: int, otp: str):
        pass

    @abc.abstractmethod
    def validate_otp(self, email: str, otp: int):
        pass

    @abc.abstractmethod
    def create_tutor(self, user_id: int, bio: str):
        pass

    @abc.abstractmethod
    def create_student(self, user_id: int):
        pass

from user.utils.base_enum import BaseEnum


class Gender(BaseEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class UserRole(BaseEnum):
    STUDENT = "STUDENT"
    TUTOR = "TUTOR"

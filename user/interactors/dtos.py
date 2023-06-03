from dataclasses import dataclass
from user.constants.enums import Gender, UserRole


@dataclass()
class RegisterUserDetailsDTO:
    first_name: str
    last_name: str
    gender: Gender
    email: str
    phone_number: int
    role: UserRole
    bio: str = None


@dataclass()
class TokenDetailsDTO:
    access_token: str
    refresh_token: str

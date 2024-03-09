from typing import Optional

from src.app.common.dto.base import DTO


class User(DTO):
    email: Optional[str]
    phone: str
    hashed_password: str


class UserUpdate(User):
    ...


class UserCreate(User):
    ...


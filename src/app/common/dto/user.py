from typing import Optional

from src.app.common.dto.base import DTO


class User(DTO):
    id: int
    email: Optional[str] = None
    phone: str
    hashed_password: str


class CreateUser(DTO):
    email: Optional[str] = None
    phone: str
    hashed_password: str


class UpdateUser(DTO):
    email: Optional[str] = None
    phone: Optional[str] = None
    hashed_password: Optional[str] = None


class DeleteUser(DTO):
    user_id: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class UpdatePartial(DTO):
    id: int
    email: Optional[str] = None
    phone: Optional[str] = None
    hashed_password: Optional[str] = None

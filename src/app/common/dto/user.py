from typing import Optional

from src.app.common.dto.base import DTO


class User(DTO):
    id: int
    email: Optional[str] = None
    phone: str
    hashed_password: str


class UserCreate(DTO):
    email: Optional[str] = None
    phone: str
    hashed_password: str


class UserUpdate(DTO):
    id: int
    email: Optional[str] = None
    phone: Optional[str] = None
    hashed_password: Optional[str] = None

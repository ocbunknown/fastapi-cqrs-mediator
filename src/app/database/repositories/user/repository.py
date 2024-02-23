from typing import Type

from src.app.database.models import User
from src.app.database.repositories.base import BaseRepository
from src.app.database.repositories.user.reader import UserReader
from src.app.database.repositories.user.writer import UserWriter


class UserRepository(BaseRepository[User]):
    __slots__ = ()
    model: Type[User] = User

    def reader(self) -> UserReader:
        return UserReader(self)

    def writer(self) -> UserWriter:
        return UserWriter(self)

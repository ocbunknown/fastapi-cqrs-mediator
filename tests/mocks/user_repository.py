from typing import Optional

from src.app.common import dto
from src.app.common.sdi.meta import SingletonMeta


class UserMock(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.users: dict[int, dto.User] = {}

    async def create(self, query: dto.User) -> dto.User | None:
        if query.id in self.users:
            return None

        self.users[query.id] = query
        return query

    async def select(
        self,
        user_id: int,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> dto.User:
        return self.users[user_id]

    async def update(
        self,
        query: dto.User,
    ) -> None:
        self.users[query.id] = query


class UserRepositoryMock:
    def reader(self) -> UserMock:
        return UserMock()

    def writer(self) -> UserMock:
        return UserMock()

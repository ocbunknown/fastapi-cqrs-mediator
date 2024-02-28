from typing import Any

from src.app.common import dto
from src.app.common.converters import convert_user_model_to_dto
from src.app.common.exceptions import NotFoundError
from src.app.database.repositories.user import UserRepository
from src.app.services import Service


class UserService(Service[UserRepository]):
    __slots__ = ("reader", "writer")

    def __init__(self, repository: UserRepository, **kwargs: Any) -> None:
        super().__init__(repository, **kwargs)
        self.reader = repository.reader()
        self.writer = repository.writer()

    async def select_user(self, user_id: int) -> dto.User:
        result = await self.reader.select(user_id)
        if not result:
            raise NotFoundError(message="User not found", status_code=404)

        return convert_user_model_to_dto(result)

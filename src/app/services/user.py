from typing import Any, Optional

from sqlalchemy.exc import IntegrityError

from src.app.common import dto
from src.app.common.converters import convert_user_model_to_dto
from src.app.common.exceptions import AlreadyExistsError, NotFoundError
from src.app.common.password import PasswordHelper
from src.app.database.repositories.user import UserRepository
from src.app.services import Service


class UserService(Service[UserRepository]):
    __slots__ = ("reader", "writer")

    def __init__(self, repository: UserRepository, **kwargs: Any) -> None:
        super().__init__(repository, **kwargs)
        self.reader = repository.reader()
        self.writer = repository.writer()
        self.password_helper = PasswordHelper()

    async def select_user(
        self,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        ) -> dto.User:
        result = await self.reader.select(user_id, email, phone)
        if not result:
            raise NotFoundError(message="User not found", status_code=404)

        return convert_user_model_to_dto(result)

    async def create_user(self, query: dto.UserCreate) -> dto.User:
        query.hashed_password = self.password_helper.hash(query.hashed_password)

        try:
            result = await self.writer.create(query)
        except IntegrityError as e:
            error_info = str(e.orig)
            if "email" in error_info:
                raise AlreadyExistsError(
                    message="This email already in use", status_code=409
                ) from e
            if "phone" in error_info:
                raise AlreadyExistsError(
                    message="This phone already in use", status_code=409
                ) from e

        if result is None:
            raise AlreadyExistsError(message="This user already exists", status_code=409)

        return convert_user_model_to_dto(result)

    async def authenticate(self, query: dto.User) -> dto.User:  # type: ignore[empty-body]
        ...

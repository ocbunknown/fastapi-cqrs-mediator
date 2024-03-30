from typing import Any, Optional

from sqlalchemy.exc import IntegrityError

from src.app.common import dto
from src.app.common.converters import (
    convert_user_model_to_delete_user_dto,
    convert_user_model_to_dto,
)
from src.app.common.exceptions import AlreadyExistsError, NotFoundError
from src.app.common.exceptions.service import InvalidParamsError
from src.app.common.password import bcrypt_hash
from src.app.database.repositories.user import UserRepository
from src.app.services import Service


class UserService(Service[UserRepository]):
    __slots__ = ("reader", "writer")

    def __init__(self, repository: UserRepository, **kwargs: Any) -> None:
        super().__init__(repository, **kwargs)
        self.reader = repository.reader()
        self.writer = repository.writer()

    async def select_user(
        self,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> dto.User:
        if not any([user_id, email, phone]):
            raise InvalidParamsError

        result = await self.reader.select(user_id, email, phone)
        if not result:
            raise NotFoundError(user_id=user_id)

        return convert_user_model_to_dto(result)

    async def create_user(self, query: dto.CreateUser) -> dto.User:
        query.hashed_password = bcrypt_hash(query.hashed_password)

        try:
            result = await self.writer.create(query)
        except IntegrityError as e:
            error_info = str(e.orig)
            if "email" in error_info:
                raise AlreadyExistsError(
                    message=f"Email: {query.email} already in use"
                ) from e
            if "phone" in error_info:
                raise AlreadyExistsError(
                    message=f"Phone: {query.phone} already in use"
                ) from e

        if not result:
            raise AlreadyExistsError

        return convert_user_model_to_dto(result)

    async def delete_user(
        self,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> dto.DeleteUser:
        if not any([user_id, email, phone]):
            raise InvalidParamsError

        result = await self.writer.delete(user_id, email, phone)
        if not result:
            raise NotFoundError(user_id=user_id)

        return convert_user_model_to_delete_user_dto(result)

    async def update_user(
        self,
        query: dto.UpdatePartial,
    ) -> dto.User:
        if query.hashed_password:
            query.hashed_password = bcrypt_hash(query.hashed_password)

        result = await self.writer.update(**query.model_dump())
        if not result:
            raise NotFoundError(user_id=query.id)

        return convert_user_model_to_dto(result)

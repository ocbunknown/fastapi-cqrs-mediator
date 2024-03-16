from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from src.app.database import models
from src.app.database.exceptions import InvalidParamsError
from src.app.database.repositories.base import BaseInteractor

if TYPE_CHECKING:
    from src.app.common import dto


class UserWriter(BaseInteractor[models.User]):
    __slots__ = ()

    async def create(self, query: dto.UserCreate) -> Optional[models.User]:
        return await self.repository.crud.create(**query.model_dump())

    async def update(
        self,
        query: dto.UserUpdate,
    ) -> Optional[models.User]:
        result = await self.repository.crud.update(
            self.repository.model.id == query.id,
            **query.model_dump(exclude_none=True),
        )
        return result[0] if result else None

    async def delete(
        self,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Optional[models.User]:
        if not any([user_id, email, phone]):
            raise InvalidParamsError("At least 1 parameter must be provided")

        if user_id:
            result = await self.repository.crud.delete(
                self.repository.model.id == user_id
            )
        elif email:
            result = await self.repository.crud.delete(
                self.repository.model.email == email
            )
        else:
            result = await self.repository.crud.delete(self.repository.model.phone == phone)

        if not result:
            return None

        return result[0]

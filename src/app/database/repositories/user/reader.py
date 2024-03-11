from __future__ import annotations
from typing import Optional, Sequence

from src.app.database import models
from src.app.database.exceptions import InvalidParamsError
from src.app.database.repositories.base import BaseInteractor


class UserReader(BaseInteractor[models.User]):
    __slots__ = ()

    async def select(
        self,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Optional[models.User]:
        if not any([user_id, email, phone]):
            raise InvalidParamsError("At least 1 parameter must be provided")

        if user_id:
            return await self.repository.crud.select(
                self.repository.model.id == user_id
            )
        if email:
            return await self.repository.crud.select(
                self.repository.model.email == email
            )

        return await self.repository.crud.select(self.repository.model.phone == phone)

    async def select_many(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Sequence[models.User]:
        return await self.repository.crud.select_many(limit=limit, offset=offset)

    async def exists(self, user_id: int) -> bool:
        return await self.repository.crud.exists(self.repository.model.id == user_id)

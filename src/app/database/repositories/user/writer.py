from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from src.app.database import models
from src.app.database.repositories.base import BaseInteractor

if TYPE_CHECKING:
    from src.app.common import dto


class UserWriter(BaseInteractor[models.User]):
    __slots__ = ()

    async def create(self, query: dto.UserCreate) -> Optional[models.User]:
        return await self.repository.crud.create(**query.model_dump())

    async def update(
        self, user_id: int, query: dto.UserUpdate
    ) -> Optional[models.User]:
        result = await self.repository.crud.update(
            self.repository.model.id == user_id, **query.model_dump(exclude_none=True)
        )
        return result[0] if result else None

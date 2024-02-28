from __future__ import annotations
from typing import Optional, Sequence

from src.app.database import models
from src.app.database.repositories.base import BaseInteractor


class UserReader(BaseInteractor[models.User]):
    __slots__ = ()

    async def select(self, user_id: int) -> Optional[models.User]:
        return await self.repository.crud.select(self.repository.model.id == user_id)

    async def select_many(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Sequence[models.User]:
        return await self.repository.crud.select_many(limit=limit, offset=offset)

    async def exists(self, user_id: int) -> bool:
        return await self.repository.crud.exists(self.repository.model.id == user_id)

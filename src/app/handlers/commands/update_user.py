from typing import Optional

from src.app.common import DTO, dto
from src.app.handlers.base import BaseHandler
from src.app.services.gateway import ServiceGateway


class UpdateUser(DTO):
    id: int
    email: Optional[str] = None
    phone: Optional[str] = None
    hashed_password: Optional[str] = None


class UpdateUserHandler(BaseHandler[UpdateUser, dto.User]):
    __slots__ = ("_gateway",)

    def __init__(self, gateway: ServiceGateway) -> None:
        self._gateway = gateway

    async def handle(self, query: UpdateUser) -> dto.User:
        async with self._gateway:
            return await self._gateway.user().update_user(query)  # type: ignore[arg-type]

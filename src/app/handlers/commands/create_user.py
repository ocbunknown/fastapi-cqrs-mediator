from typing import Optional

from src.app.common import DTO, dto
from src.app.handlers.base import BaseHandler
from src.app.services.gateway import ServiceGateway


class CreateUser(DTO):
    email: Optional[str] = None
    phone: str
    hashed_password: str


class CreateUserHandler(BaseHandler[CreateUser, dto.User]):
    __slots__ = ("_gateway",)

    def __init__(self, gateway: ServiceGateway) -> None:
        self._gateway = gateway

    async def handle(self, query: CreateUser) -> dto.User:
        async with self._gateway:
            return await self._gateway.user().create_user(query) #type: ignore[arg-type]

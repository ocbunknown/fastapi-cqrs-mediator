from src.app.common import dto
from src.app.handlers.base import BaseHandler
from src.app.services.gateway import ServiceGateway


class UpdateUserHandler(BaseHandler[dto.UserUpdate, dto.User]):
    __slots__ = ("_gateway",)

    def __init__(self, gateway: ServiceGateway) -> None:
        self._gateway = gateway

    async def handle(self, query: dto.UserUpdate) -> dto.User:
        async with self._gateway:
            return await self._gateway.user().update_user(query)


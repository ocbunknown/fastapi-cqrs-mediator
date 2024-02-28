from typing import Any, Coroutine

from src.app.common import dto
from src.app.handlers.base import BaseHandler
from src.app.services.gateway import ServiceGateway


class SelectUserHandler(BaseHandler[int, dto.User]):
    __slots__ = ("_gateway",)

    def __init__(self, gateway: ServiceGateway) -> None:
        self._gateway = gateway

    async def handler(self, query: int) -> Coroutine[Any, Any, dto.User]:
        async with self._gateway:
            return await self._gateway.user().select_user(user_id=query)




from pydantic import BaseModel

from src.app.common import dto
from src.app.handlers.base import BaseHandler
from src.app.services.gateway import ServiceGateway


class GetUserQuery(BaseModel):
    user_id: int


class GetUserHandler(BaseHandler[GetUserQuery, dto.User]):
    __slots__ = ("_gateway",)

    def __init__(self, gateway: ServiceGateway) -> None:
        self._gateway = gateway

    async def handle(self, query: GetUserQuery) -> dto.User:
        async with self._gateway:
            return await self._gateway.user().select_user(**query.model_dump())

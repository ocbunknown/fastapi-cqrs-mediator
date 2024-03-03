from types import TracebackType
from typing import Optional, Type

from typing_extensions import Self

from src.app.database import (
    DatabaseGateway,
    database_gateway_factory,
    sa_unit_of_work_factory,
)
from src.app.database.core.connection import SessionFactoryType
from src.app.services.user import UserService


class ServiceGateway:
    __slots__ = ("db_gateway",)

    def __init__(self, db_gateway: DatabaseGateway) -> None:
        self.db_gateway = db_gateway

    async def __aenter__(self: Self) -> Self:
        await self.db_gateway.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.db_gateway.__aexit__(exc_type, exc_value, traceback)

    def user(self) -> UserService:
        return UserService(self.db_gateway.user())


def service_gateway_factory(
    session_factory: SessionFactoryType,
) -> ServiceGateway:
    session = session_factory()
    return ServiceGateway(database_gateway_factory(sa_unit_of_work_factory(session)))

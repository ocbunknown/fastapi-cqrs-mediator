from types import TracebackType
from typing import Optional, Type, TypeVar

from src.app.database.core.uow import SQLAlchemyUnitOfWork
# from src.app.database.repositories import UserRepository

Self = TypeVar("Self", bound="DatabaseGateway")


class DatabaseGateway:
    __slots__ = ("uow",)

    def __init__(self, unit_of_work: SQLAlchemyUnitOfWork) -> None:
        self.uow = unit_of_work

    async def __aenter__(self: Self) -> Self:
        await self.uow.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self.uow.__aexit__(exc_type, exc_value, traceback)

    # def user(self) -> UserRepository:
    #     return UserRepository(self.uow.session)


def database_gateway_factory(unit_of_work: SQLAlchemyUnitOfWork) -> DatabaseGateway:
    return DatabaseGateway(unit_of_work)

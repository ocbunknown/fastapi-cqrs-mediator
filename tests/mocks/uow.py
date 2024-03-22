from types import TracebackType
from typing import Optional, Type

from typing_extensions import Self


class SQLAlchemyUnitOfWorkMock:
    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        return None

    async def commit(self) -> None:
        ...

    async def rollback(self) -> None:
        ...

    async def create_transaction(self) -> None:
        ...

    async def close_transaction(self) -> None:
        ...

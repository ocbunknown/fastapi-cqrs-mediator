from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Mapping,
    Optional,
    Sequence,
    TypeVar,
    cast,
)

from sqlalchemy import (
    ColumnExpressionArgument,
    CursorResult,
    delete,
    exists,
    func,
    insert,
    select,
    update,
)

from src.app.common.interfaces.crud import AbstractCRUDRepository
from src.app.database.models.base.core import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType", bound=Base)


class SQLAlchemyCRUDRepository(
    AbstractCRUDRepository[ModelType, ColumnExpressionArgument[bool]]
):
    """Repository class for CRUD (Create, Read, Update, Delete) operations using SQLAlchemy with asynchronous support.

    Args:
    ----
        session (AsyncSession): The SQLAlchemy asynchronous session to be used for database operations.
        model (Type[ModelType]): The SQLAlchemy model type associated with the repository.

    Attributes:
    ----------
        _session (AsyncSession): The SQLAlchemy asynchronous session associated with the repository.

    """

    __slots__ = ("_session",)

    def __init__(self, session: AsyncSession, model: type[ModelType]) -> None:
        """Initialize the repository with the provided asynchronous session and model type.

        Args:
        ----
            session (AsyncSession): The SQLAlchemy asynchronous session to be used for database operations.
            model (Type[ModelType]): The SQLAlchemy model type associated with the repository.

        """
        super().__init__(model)
        self._session = session

    async def create(self, **values: Any) -> Optional[ModelType]:
        """Create a new entry in the data storage using the provided values.

        Args:
        ----
            **values (Mapping[str, Any]): Keyword arguments representing the values to be stored.

        Returns:
        -------
            Optional[ModelType]: The created entry if successful, or None if the creation fails.

        """
        stmt = insert(self.model).values(**values).returning(self.model)
        return (await self._session.execute(stmt)).scalars().first()

    async def create_many(
        self, data: Sequence[Mapping[str, Any]]
    ) -> Sequence[ModelType]:
        """Create multiple entries in the data storage using the provided data.

        Args:
        ----
            data (Sequence[Mapping[str, Any]]): A sequence of dictionaries representing data for multiple entries.

        Returns:
        -------
            Sequence[ModelType]: A sequence of created entries.

        """
        stmt = insert(self.model).returning(self.model)
        result = await self._session.scalars(stmt, data)
        return result.all()

    async def select(
        self,
        *clauses: ColumnExpressionArgument[bool],
    ) -> Optional[ModelType]:
        """Select and retrieve an entry from the data storage based on the provided clauses.

        Args:
        ----
            *clauses (ColumnExpressionArgument[bool]): Columns or conditions used for selection.

        Returns:
        -------
            Optional[ModelType]: The selected entry if found, or None if no matching entry is found.

        """
        stmt = select(self.model).where(*clauses)
        return (await self._session.execute(stmt)).scalars().first()

    async def select_many(
        self,
        *clauses: ColumnExpressionArgument[bool],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Sequence[ModelType]:
        """Select and retrieve multiple entries from the data storage based on the provided clauses and pagination options.

        Args:
        ----
            *clauses (ColumnExpressionArgument[bool]): Columns or conditions used for selection.
            offset (Optional[int]): Offset for pagination.
            limit (Optional[int]): Maximum number of entries to retrieve.

        Returns:
        -------
            Sequence[ModelType]: A sequence of selected entries.

        """
        stmt = select(self.model).where(*clauses).offset(offset).limit(limit)
        return (await self._session.execute(stmt)).scalars().all()

    async def update(
        self, *clauses: ColumnExpressionArgument[bool], **values: Any
    ) -> Sequence[ModelType]:
        """Update one or more entries in the data storage based on the provided clauses and values.

        Args:
        ----
            *clauses (ColumnExpressionArgument[bool]): Columns or conditions used for selection and update.
            **values (Mapping[str, Any]): Keyword arguments representing the values to update.

        Returns:
        -------
            Sequence[ModelType]: A sequence of updated entries.

        """
        stmt = update(self.model).where(*clauses).values(**values).returning(self.model)
        return (await self._session.execute(stmt)).scalars().all()

    async def update_many(self, data: Sequence[Mapping[str, Any]]) -> CursorResult[Any]:
        """Update multiple entries in the data storage using the provided data.

        Args:
        ----
            data (Sequence[Mapping[str, Any]]): A sequence of dictionaries representing data for updating multiple entries.

        Returns:
        -------
            CursorResult[Any]: Implementation-specific return value indicating the result of the update operation.

        """
        return await self._session.execute(update(self.model), data)

    async def delete(
        self, *clauses: ColumnExpressionArgument[bool]
    ) -> Sequence[ModelType]:
        """Delete one or more entries from the data storage based on the provided clauses.

        Args:
        ----
            *clauses (ColumnExpressionArgument[bool]): Columns or conditions used for selection and deletion.

        Returns:
        -------
            Sequence[ModelType]: A sequence of deleted entries.

        """
        stmt = delete(self.model).where(*clauses).returning(self.model)
        return (await self._session.execute(stmt)).scalars().all()

    async def exists(self, *clauses: ColumnExpressionArgument[bool]) -> bool:
        """Check if an entry matching the provided clauses exists in the data storage.

        Args:
        ----
            *clauses (ColumnExpressionArgument[bool]): Columns or conditions used for existence check.

        Returns:
        -------
            bool: True if an entry exists, False otherwise.

        """
        stmt = exists(select(self.model).where(*clauses)).select()
        return cast(bool, await self._session.scalar(stmt))

    async def count(self, *clauses: ColumnExpressionArgument[bool]) -> int:
        """Count the number of entries in the data storage based on the provided clauses.

        Args:
        ----
            *clauses (ColumnExpressionArgument[bool]): Columns or conditions used for counting.

        Returns:
        -------
            int: The count of entries that match the provided clauses.

        """
        stmt = select(func.count()).where(*clauses).select_from(self.model)
        return cast(int, await self._session.scalar(stmt))

    def with_query_model(
        self, model: type[ModelType]
    ) -> SQLAlchemyCRUDRepository[ModelType]:
        return SQLAlchemyCRUDRepository(self._session, model)

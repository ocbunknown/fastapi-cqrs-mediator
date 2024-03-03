import abc
from typing import (
    Any,
    Generic,
    Mapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from src.app.common.interfaces.repository import Repository

EntryType = TypeVar("EntryType")
ColumnType = TypeVar("ColumnType")


class AbstractCRUDRepository(Repository, Generic[EntryType, ColumnType]):
    """Abstract base class for CRUD (Create, Read, Update, Delete) repositories.

    This class defines the common interface for repository classes that interact with data storage.

    Args:
    ----
        model (Type[EntryType]): The model type that the repository operates on.

    Attributes:
    ----------
        model (Type[EntryType]): The model type that the repository operates on.

    """

    model: Type[EntryType]

    def __init__(self, model: Type[EntryType]) -> None:
        """Initialize the repository with the specified model type.

        Args:
        ----
            model (Type[EntryType]): The model type that the repository operates on.

        """
        self.model = model

    @abc.abstractmethod
    async def create(self, **values: Mapping[str, Any]) -> Optional[EntryType]:
        """Create a new entry in the data storage using the provided values.

        Args:
        ----
            **values (Mapping[str, Any]): Keyword arguments representing the values to be stored.

        Returns:
        -------
            Optional[EntryType]: The created entry if successful, or None if the creation fails.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def create_many(
        self, data: Sequence[Mapping[str, Any]]
    ) -> Sequence[EntryType]:
        """Create multiple entries in the data storage using the provided data.

        Args:
        ----
            data (Sequence[Mapping[str, Any]]): A sequence of dictionaries representing data for multiple entries.

        Returns:
        -------
            Sequence[EntryType]: A sequence of created entries.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def select(
        self,
        *clauses: ColumnType,
    ) -> Optional[EntryType]:
        """Select and retrieve an entry from the data storage based on the provided clauses.

        Args:
        ----
            *clauses (ColumnType): Columns or conditions used for selection.

        Returns:
        -------
            Optional[EntryType]: The selected entry if found, or None if no matching entry is found.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def select_many(
        self,
        *clauses: ColumnType,
        offset: Optional[int],
        limit: Optional[int],
    ) -> Sequence[EntryType]:
        """Select and retrieve multiple entries from the data storage based on the provided clauses and pagination options.

        Args:
        ----
            *clauses (ColumnType): Columns or conditions used for selection.
            offset (Optional[int]): Offset for pagination.
            limit (Optional[int]): Maximum number of entries to retrieve.

        Returns:
        -------
            Sequence[EntryType]: A sequence of selected entries.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def update(
        self, *clauses: ColumnType, **values: Mapping[str, Any]
    ) -> Sequence[EntryType]:
        """Update one or more entries in the data storage based on the provided clauses and values.

        Args:
        ----
            *clauses (ColumnType): Columns or conditions used for selection and update.
            **values (Mapping[str, Any]): Keyword arguments representing the values to update.

        Returns:
        -------
            Sequence[EntryType]: A sequence of updated entries.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def update_many(self, data: Sequence[Mapping[str, Any]]) -> Any:
        """Update multiple entries in the data storage using the provided data.

        Args:
        ----
            data (Sequence[Mapping[str, Any]]): A sequence of dictionaries representing data for updating multiple entries.

        Returns:
        -------
            Any: Implementation-specific return value indicating the result of the update operation.

        """
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, *clauses: ColumnType) -> Sequence[EntryType]:
        """Delete one or more entries from the data storage based on the provided clauses.

        Args:
        ----
            *clauses (ColumnType): Columns or conditions used for selection and deletion.

        Returns:
        -------
            Sequence[EntryType]: A sequence of deleted entries.

        """
        raise NotImplementedError

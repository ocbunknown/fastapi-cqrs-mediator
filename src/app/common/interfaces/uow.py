from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Generic, Optional, Protocol, TypeVar

if TYPE_CHECKING:
    from types import TracebackType

SessionType = TypeVar("SessionType")
TransactionType = TypeVar("TransactionType")
Self = TypeVar("Self", bound="UnitOfWork")


class UnitOfWork(Protocol):
    """An abstract protocol defining the interface for a Unit of Work.

    A Unit of Work is responsible for managing transactions and the lifecycle
    of database operations.

    """

    @abc.abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Asynchronous context manager exit method for handling transactions.

        :param exc_type: The type of exception, if any.
        :type exc_type: Optional[Type[BaseException]]
        :param exc_value: The exception instance, if any.
        :type exc_value: Optional[BaseException]
        :param traceback: The traceback information, if any.
        :type traceback: Optional[TracebackType]
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def __aenter__(self: Self) -> Self:
        """Asynchronous context manager enter method for starting a transaction.

        :return: The unit of work instance.
        :rtype: Self
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def commit(self) -> None:
        """Commit the changes made during the unit of work.

        This method should be implemented in subclasses.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def rollback(self) -> None:
        """Rollback the changes made during the unit of work.

        This method should be implemented in subclasses.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def create_transaction(self) -> None:
        """Create a new transaction within the unit of work.

        This method should be implemented in subclasses.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def close_transaction(self) -> None:
        """Close the transaction within the unit of work.

        This method should be implemented in subclasses.
        """
        raise NotImplementedError


class AbstractUnitOfWork(UnitOfWork, Generic[SessionType, TransactionType]):
    """An abstract base class for implementing the Unit of Work pattern.

    This class provides a generic interface for managing a unit of work
    involving a database session and transactions.

    :param session: The session associated with the unit of work.
    :type session: SessionType
    """

    __slots__ = ("session", "_transaction")

    def __init__(self, session: SessionType) -> None:
        """Initialize a new instance of the AbstractUnitOfWork class.

        :param session: The session associated with the unit of work.
        :type session: SessionType
        """
        self.session = session
        self._transaction: Optional[TransactionType] = None

    async def __aenter__(self) -> AbstractUnitOfWork[SessionType, TransactionType]:
        """Enter the unit of work context and create a transaction if needed.

        :return: The unit of work instance.
        :rtype: AbstractUnitOfWork[SessionType, TransactionType]
        """
        await self.create_transaction()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Exit the unit of work context and commit or rollback the transaction accordingly.

        :param exc_type: The type of exception, if any.
        :type exc_type: Optional[Type[BaseException]]
        :param exc_value: The exception instance, if any.
        :type exc_value: Optional[BaseException]
        :param traceback: The traceback information, if any.
        :type traceback: Optional[TracebackType]
        """
        if self._transaction:
            if exc_type:
                await self.rollback()
            else:
                await self.commit()

        await self.close_transaction()

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction

from src.app.common.interfaces.uow import AbstractUnitOfWork
from src.app.database.exceptions import CommitError, RollbackError


class SQLAlchemyUnitOfWork(AbstractUnitOfWork[AsyncSession, AsyncSessionTransaction]):
    """Represents a unit of work (UoW) for managing transactions and database operations using SQLAlchemy with asynchronous support.

    This class implements the AbstractUnitOfWork interface and provides methods for committing and rolling back transactions,
    as well as creating and closing transactions using an SQLAlchemy AsyncSession.

    Args:
    ----
        session (AsyncSession): The SQLAlchemy asynchronous session to be used for database operations within the unit of work.

    Attributes:
    ----------
        _session (AsyncSession): The asynchronous session associated with the unit of work.
        _transaction (AsyncSessionTransaction): The current transaction within the unit of work.

    Raises:
    ------
        CommitError: If an error occurs while attempting to commit the transaction.
        RollbackError: If an error occurs while attempting to rollback the transaction.

    """

    async def commit(self) -> None:
        """Commit the current transaction within the unit of work.

        Raises
        ------
            CommitError: If an error occurs while attempting to commit the transaction.

        """
        try:
            await self.session.commit()
        except SQLAlchemyError as err:
            raise CommitError from err

    async def rollback(self) -> None:
        """Rollback the current transaction within the unit of work.

        Raises
        ------
            RollbackError: If an error occurs while attempting to rollback the transaction.

        """
        try:
            await self.session.rollback()
        except SQLAlchemyError as err:
            raise RollbackError from err

    async def create_transaction(self) -> None:
        """Create a new transaction if one does not already exist and the session is active.

        This method is internal and should not be called directly.

        Note:
        ----
            This method is intended for internal use and is automatically called when necessary.

        """
        if not self.session.in_transaction() and self.session.is_active:
            self._transaction = await self.session.begin()

    async def close_transaction(self) -> None:
        """Close the current transaction within the unit of work if the session is active.

        This method is internal and should not be called directly.

        Note:
        ----
            This method is intended for internal use and is automatically called when necessary.

        """
        if self.session.is_active:
            await self.session.close()


def sa_unit_of_work_factory(session: AsyncSession) -> SQLAlchemyUnitOfWork:
    return SQLAlchemyUnitOfWork(session)

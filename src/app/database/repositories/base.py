from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from src.app.common.interfaces.repository import Repository
from src.app.database.repositories.crud import ModelType, SQLAlchemyCRUDRepository

RepositoryType = TypeVar("RepositoryType", bound=Repository)


class BaseRepository(Repository, Generic[ModelType]):
    """Base repository class for interacting with a specific SQLAlchemy model using asynchronous sessions.

    Args:
    ----
        session (AsyncSession): The SQLAlchemy asynchronous session to be used for database operations.

    Attributes:
    ----------
        _session (AsyncSession): The SQLAlchemy asynchronous session associated with the repository.
        _crud (SQLAlchemyCRUDRepository[ModelType]): The CRUD repository for the specific model.

    """

    __slots__ = (
        "model",
        "_session",
        "_crud",
    )
    model: Type[ModelType]

    def __init__(self, session: AsyncSession) -> None:
        """Initialize the repository with the provided asynchronous session.

        Args:
        ----
            session (AsyncSession): The SQLAlchemy asynchronous session to be used for database operations.

        """
        self._session = session
        self._crud = SQLAlchemyCRUDRepository(session, self.model)


class BaseInteractor(Generic[ModelType]):
    __slots__ = ("repository",)

    def __init__(self, repository: BaseRepository[ModelType]) -> None:
        self.repository = repository

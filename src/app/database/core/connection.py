from typing import AsyncIterable

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# Type alias for the session factory
SessionFactoryType = async_sessionmaker[AsyncSession]


class Connection:
    def __init__(self, url: str, *, echo: bool = False) -> None:
        """Initialize Connection class.

        Args:
        ----
            url (str): The database URL.
            echo (bool): Enable/Disable SQLAlchemy logs.

        """
        self.engine = create_async_engine(url=url, echo=echo)

    def create_sa_session_factory(self) -> SessionFactoryType:
        """Create a session factory for asynchronous SQLAlchemy sessions.

        Args:
        ----
            engine (AsyncEngine): An asynchronous SQLAlchemy engine.

        Returns:
        -------
            SessionFactoryType: A session factory for creating asynchronous sessions.

        """
        return async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def create_sa_session(self) -> AsyncIterable[AsyncSession]:
        """Create an asynchronous SQLAlchemy session.

        Args:
        ----
            session_factory (SessionFactoryType): A session factory for creating asynchronous sessions.

        Yields:
        ------
            Iterator[AsyncSession]: An asynchronous SQLAlchemy session.

        """
        session_factory: SessionFactoryType = self.create_sa_session_factory()

        async with session_factory() as session:
            yield session

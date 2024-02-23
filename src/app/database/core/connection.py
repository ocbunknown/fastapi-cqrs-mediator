from typing import Any, AsyncIterable

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# Type alias for the session factory
SessionFactoryType = async_sessionmaker[AsyncSession]


def create_sa_engine(url: str, **kwargs: Any) -> AsyncEngine:
    """Create an asynchronous SQLAlchemy engine.

    Args:
    ----
        url (str): The database URL.
        **kwargs: Additional keyword arguments to pass to create_async_engine.

    Returns:
    -------
        AsyncEngine: An asynchronous SQLAlchemy engine.

    """
    return create_async_engine(url, **kwargs)


def create_sa_session_factory(engine: AsyncEngine) -> SessionFactoryType:
    """Create a session factory for asynchronous SQLAlchemy sessions.

    Args:
    ----
        engine (AsyncEngine): An asynchronous SQLAlchemy engine.

    Returns:
    -------
        SessionFactoryType: A session factory for creating asynchronous sessions.

    """
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def create_sa_session(
    session_factory: SessionFactoryType,
) -> AsyncIterable[AsyncSession]:
    """Create an asynchronous SQLAlchemy session.

    Args:
    ----
        session_factory (SessionFactoryType): A session factory for creating asynchronous sessions.

    Yields:
    ------
        Iterator[AsyncSession]: An asynchronous SQLAlchemy session.

    """
    async with session_factory() as session:
        yield session

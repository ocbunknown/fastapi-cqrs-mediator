from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.database.core.gateway import DatabaseGateway, database_gateway_factory
from src.app.database.core.uow import SQLAlchemyUnitOfWork, sa_unit_of_work_factory

__all__ = (
    "DatabaseGateway",
    "SQLAlchemyUnitOfWork",
    "database_gateway_factory",
    "sa_unit_of_work_factory",
    "transaction_gateway",
    "session_gateway",
)


async def transaction_gateway(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[DatabaseGateway]:
    session = session_factory()
    gateway = database_gateway_factory(sa_unit_of_work_factory(session))
    async with gateway:
        yield gateway


async def session_gateway(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[DatabaseGateway]:
    session = session_factory()
    gateway = database_gateway_factory(sa_unit_of_work_factory(session))
    async with session:
        yield gateway
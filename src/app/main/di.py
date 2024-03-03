from typing import Callable, TypeVar

from fastapi import FastAPI

from src.app.core.config import load_settings
from src.app.database.core.connection import create_sa_engine, create_sa_session_factory
from src.app.handlers.queries import build_query_mediator
from src.app.handlers.queries.mediator import QueryMediator

DependencyType = TypeVar("DependencyType")


def singleton(dependency: DependencyType) -> Callable[[], DependencyType]:
    def singleton_factory() -> DependencyType:
        return dependency

    return singleton_factory


def init_dependencies(app: FastAPI) -> None:
    settings = load_settings()
    engine = create_sa_engine(settings.db.url)
    session_factory = create_sa_session_factory(engine)

    query_mediator = QueryMediator()
    build_query_mediator(query_mediator, session_factory)

    app.dependency_overrides[QueryMediator] = singleton(query_mediator)

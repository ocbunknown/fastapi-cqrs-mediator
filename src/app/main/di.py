from typing import Callable, TypeVar

from fastapi import FastAPI

from src.app.database.core.connection import create_sa_engine, create_sa_session_factory
from src.app.handlers.commands.mediator import CommandMediator
from src.app.handlers.commands.setup import build_command_mediator
from src.app.handlers.queries import build_query_mediator
from src.app.handlers.queries.mediator import QueryMediator
from src.app.settings.config import load_settings

DependencyType = TypeVar("DependencyType")


def singleton(dependency: DependencyType) -> Callable[[], DependencyType]:
    def singleton_factory() -> DependencyType:
        return dependency

    return singleton_factory


def init_dependencies(app: FastAPI) -> None:
    settings = load_settings()
    engine = create_sa_engine(settings.url)
    session_factory = create_sa_session_factory(engine)

    query_mediator = QueryMediator()
    command_mediator = CommandMediator()
    build_query_mediator(query_mediator, session_factory)
    build_command_mediator(command_mediator, session_factory)

    app.dependency_overrides[QueryMediator] = singleton(query_mediator)
    app.dependency_overrides[CommandMediator] = singleton(command_mediator)

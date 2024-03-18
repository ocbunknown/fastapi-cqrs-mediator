from src.app.database.core.connection import SessionFactoryType
from src.app.handlers import queries
from src.app.handlers.queries import QueryMediator
from src.app.services.gateway import service_gateway_factory


def build_query_mediator(
    mediator: QueryMediator,
    session_factory: SessionFactoryType,
) -> None:
    dependencies = (
        (queries.GetUser, queries.GetUserHandler),
    )
    for q, handler in dependencies:
        mediator.register(
            q,
            lambda handler=handler: handler(service_gateway_factory(session_factory)),
        )

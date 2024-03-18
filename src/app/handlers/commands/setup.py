from src.app.database.core.connection import SessionFactoryType
from src.app.handlers import commands
from src.app.handlers.commands import CommandMediator
from src.app.services.gateway import service_gateway_factory


def build_command_mediator(
    mediator: CommandMediator,
    session_factory: SessionFactoryType,
) -> None:
    dependencies = (
        (commands.CreateUser, commands.CreateUserHandler),
        (commands.DeleteUser, commands.DeleteUserHandler),
        (commands.UpdateUser, commands.UpdateUserHandler),
    )
    for q, handler in dependencies:
        mediator.register(
            q,  # type: ignore[arg-type]
            lambda handler=handler: handler(service_gateway_factory(session_factory)),
        )

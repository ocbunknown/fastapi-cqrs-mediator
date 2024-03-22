from src.app.common import dto
from src.app.handlers.commands import CreateUserHandler
from src.app.services.gateway import ServiceGateway


async def test_create_user_handler(
    service_gateway: ServiceGateway,
    valid_user: dto.User,
) -> None:
    handler = await CreateUserHandler(service_gateway).handle(
        dto.User(**valid_user.model_dump())  # type: ignore
    )

    assert handler.id == valid_user.id
    assert handler.phone == valid_user.phone
    assert handler.email == valid_user.email

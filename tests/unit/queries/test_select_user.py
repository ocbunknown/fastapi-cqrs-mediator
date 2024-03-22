from src.app.common import dto
from src.app.handlers.queries import GetUser, GetUserHandler
from src.app.services.gateway import ServiceGateway


async def test_get_user_handler(
    service_gateway: ServiceGateway,
    valid_user: dto.User,
) -> None:
    handler = await GetUserHandler(service_gateway).handle(
        GetUser(user_id=valid_user.id)
    )

    assert handler.id == valid_user.id
    assert handler.phone == valid_user.phone
    assert handler.email == valid_user.email

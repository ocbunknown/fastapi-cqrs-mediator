import pytest

from src.app.common import dto
from src.app.services.gateway import ServiceGateway
from tests.mocks.gateway import DatabaseGatewayMock, database_gateway_factory


@pytest.fixture()
def db_gateway() -> DatabaseGatewayMock:
    return database_gateway_factory()


@pytest.fixture()
def service_gateway(db_gateway: DatabaseGatewayMock) -> ServiceGateway:
    return ServiceGateway(db_gateway)  # type: ignore[arg-type]


@pytest.fixture()
def valid_user() -> dto.User:
    return dto.User(
        id=1,
        email="my@gmail.com",
        phone="+00000000",
        hashed_password="strong",
    )

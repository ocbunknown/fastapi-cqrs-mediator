from functools import partial

from fastapi import FastAPI

from src.app.common.markers import SessionGatewayMarker, TransactionGatewayMarker
from src.app.core.config import load_settings
from src.app.database import session_gateway
from src.app.database.core.connection import create_sa_engine, create_sa_session_factory
from src.app.services.gateway import service_gateway_factory


def init_dependencies(app: FastAPI) -> None:
    settings = load_settings()
    engine = create_sa_engine(settings.db.url)
    session_factory = create_sa_session_factory(engine)

    app.dependency_overrides[TransactionGatewayMarker] = partial(
        service_gateway_factory, session_factory
    )
    app.dependency_overrides[SessionGatewayMarker] = partial(
        session_gateway, session_factory
    )

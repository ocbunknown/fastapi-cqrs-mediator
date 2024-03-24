from fastapi import APIRouter, FastAPI

from src.app.api.endpoints.v1.healthcheck import healthcheck_router
from src.app.api.endpoints.v1.user import user_router


def init_routers(app: FastAPI) -> None:
    root_router = APIRouter(prefix="/api")

    root_router.include_router(healthcheck_router)
    root_router.include_router(user_router)

    app.include_router(root_router)

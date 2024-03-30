from fastapi import APIRouter, FastAPI

from src.app.api.endpoints.v1 import v1_router


def init_routers(app: FastAPI) -> None:
    root_router = APIRouter(prefix="/api")
    root_router.include_router(v1_router)

    app.include_router(root_router)

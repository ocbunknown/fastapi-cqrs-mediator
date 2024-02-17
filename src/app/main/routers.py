from fastapi import FastAPI

from src.app.api import root_router


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)

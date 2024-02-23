from fastapi import FastAPI

from src.app.main.di import init_dependencies
from src.app.main.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    return app

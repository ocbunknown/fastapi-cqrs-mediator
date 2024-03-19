from fastapi import FastAPI

from src.app.main.di import init_dependencies
from src.app.main.exceptions import init_exception_handlers
from src.app.main.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    init_exception_handlers(app)
    return app

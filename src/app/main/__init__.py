__all__ = (
    "create_app",
    "init_routers",
)

from src.app.main.routers import init_routers
from src.app.main.web import create_app

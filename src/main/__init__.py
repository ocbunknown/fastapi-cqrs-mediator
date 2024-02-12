__all__ = [
    "create_app",
    "init_routers",
]

from src.main.routers import init_routers
from src.main.web import create_app

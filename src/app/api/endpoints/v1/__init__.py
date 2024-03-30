from fastapi import APIRouter

from src.app.api.endpoints.healthcheck import healthcheck_router
from src.app.api.endpoints.v1.user import user_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(healthcheck_router)
v1_router.include_router(user_router)

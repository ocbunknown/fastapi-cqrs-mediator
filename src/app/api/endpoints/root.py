from fastapi import APIRouter

from src.app.api.endpoints.user import user_router

root_router = APIRouter(prefix="/api")

root_router.include_router(user_router)

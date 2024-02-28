from fastapi import APIRouter

from src.app.api.endpoints.hotel import hotel_router

root_router = APIRouter()

root_router.include_router(hotel_router)

from fastapi import APIRouter

from src.app.api.hotel import hotel_router

root_router = APIRouter()

root_router.include_router(hotel_router)

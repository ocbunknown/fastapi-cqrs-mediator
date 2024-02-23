from typing import Annotated

from fastapi import APIRouter, Depends

from src.app.common.dto.user import UserDTO
from src.app.common.markers import TransactionGatewayMarker
from src.app.database import DatabaseGateway

hotel_router = APIRouter(tags=["Find Hotel"])


@hotel_router.get("/", response_model=UserDTO)
async def get_user(
    gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)],
) -> UserDTO:
    return await gateway.user().reader().select(user_id=1)

from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.app.api.responses import OkResponse
from src.app.common import dto
from src.app.common.markers import TransactionGatewayMarker
from src.app.services.gateway import ServiceGateway

hotel_router = APIRouter(tags=["Find Hotel"])


@hotel_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
)
async def get_user(
    gateway: Annotated[ServiceGateway, Depends(TransactionGatewayMarker)],
) -> OkResponse[dto.User]:
    result = await gateway.user().select_user(user_id=1)
    return OkResponse(result, status_code=status.HTTP_200_OK)

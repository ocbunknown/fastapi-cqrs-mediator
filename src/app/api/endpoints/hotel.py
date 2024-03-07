from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.app.api.responses import OkResponse
from src.app.common import dto
from src.app.handlers.queries import GetUserQuery, QueryMediator

hotel_router = APIRouter(tags=["Find Hotel"])


@hotel_router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
)
async def get_user(
    user_id: int,
    mediator: Annotated[QueryMediator, Depends()],
) -> OkResponse[dto.User]:
    return OkResponse(await mediator(GetUserQuery(user_id=user_id)))

from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.app.common import dto
from src.app.core.depends_stub import Stub
from src.app.handlers.queries import GetUserQuery, QueryMediator

hotel_router = APIRouter(tags=["Find Hotel"])


@hotel_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
)
async def get_user(
    user_id: int,
    mediator: Annotated[QueryMediator, Depends(Stub(QueryMediator))],
) -> dto.User:
    return await mediator(GetUserQuery(user_id=user_id))

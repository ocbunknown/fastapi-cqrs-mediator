from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status

from src.app.api.responses import OkResponse
from src.app.common import dto
from src.app.handlers.commands import CommandMediator
from src.app.handlers.queries import GetUserQuery, QueryMediator
from pydantic import BaseModel
user_router = APIRouter(prefix="/v1/users", tags=["User"])



@user_router.post(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
    description="Create User Endpoint",
)
async def create_user_endpoint(
    mediator: Annotated[CommandMediator, Depends()],
    body: dto.UserCreate,
) -> OkResponse[dto.User]:
    return OkResponse(
        await mediator(body)
    )


@user_router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
    description="Get User Endpoint",
)
async def get_user_by_id_endpoint(
    mediator: Annotated[QueryMediator, Depends()],
    user_id: int,
) -> OkResponse[dto.User]:
    return OkResponse(
        await mediator(
            GetUserQuery(
                user_id=user_id,
            )
        ),
    )

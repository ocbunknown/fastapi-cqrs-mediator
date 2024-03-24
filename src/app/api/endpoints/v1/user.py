from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.app.api.responses import OkResponse
from src.app.common import dto
from src.app.handlers.commands import (
    CommandMediator,
    CreateUser,
    DeleteUser,
    UpdateUser,
)
from src.app.handlers.queries import GetUser, QueryMediator

user_router = APIRouter(prefix="/v1/users", tags=["User"])


@user_router.post(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
)
async def create_user_endpoint(
    mediator: Annotated[CommandMediator, Depends()],
    body: CreateUser,
) -> OkResponse[dto.User]:
    return OkResponse(
        await mediator(body),
    )


@user_router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
)
async def get_user_by_id_endpoint(
    mediator: Annotated[QueryMediator, Depends()],
    user_id: int,
) -> OkResponse[dto.User]:
    return OkResponse(
        await mediator(GetUser(user_id=user_id)),
    )


@user_router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=dto.DeleteUser,
)
async def delete_user_endpoint(
    mediator: Annotated[CommandMediator, Depends()],
    user_id: int,
) -> OkResponse[dto.DeleteUser]:
    return OkResponse(
        await mediator(DeleteUser(user_id=user_id)),
    )


@user_router.patch(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=dto.User,
)
async def update_user_endpoint(
    mediator: Annotated[CommandMediator, Depends()],
    user_id: int,
    body: dto.UpdateUser,
) -> OkResponse[dto.User]:
    return OkResponse(
        await mediator(UpdateUser(id=user_id, **body.model_dump())),
    )

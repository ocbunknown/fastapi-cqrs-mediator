from collections.abc import Awaitable, Callable
from functools import partial

from fastapi import FastAPI
from starlette import status
from starlette.requests import Request

from src.app.api.responses import ORJSONResponse
from src.app.common.exceptions import (
    AlreadyExistsError,
    AppException,
    InvalidParamsError,
    NotFoundError,
)
from src.app.common.exceptions.responses import ErrorResponse


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        AppException,
        error_handler(500),
    )
    app.add_exception_handler(
        NotFoundError,
        error_handler(status.HTTP_404_NOT_FOUND),
    )
    app.add_exception_handler(
        AlreadyExistsError,
        error_handler(status.HTTP_409_CONFLICT),
    )
    app.add_exception_handler(
        InvalidParamsError,
        error_handler(status.HTTP_400_BAD_REQUEST),
    )
    app.add_exception_handler(
        Exception,
        unknown_exception_handler,
    )


def error_handler(status_code: int) -> Callable[..., Awaitable[ORJSONResponse]]:
    return partial(app_error_handler, status_code=status_code)


async def app_error_handler(
    request: Request, err: AppException, status_code: int
) -> ORJSONResponse:
    return await handle_error(
        request=request,
        err=err,
        err_data=err.title,
        status_code=status_code,
    )


async def unknown_exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResponse(error=err),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_error(
    request: Request,
    err: Exception,
    err_data: str,
    status_code: int,
) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResponse(error=err_data, status=status_code),
        status_code=status_code,
    )

from typing import Generic, Mapping, Optional, TypeVar

from fastapi.responses import Response
from starlette.background import BackgroundTask

ResultType = TypeVar("ResultType")


class OkResponse(Response, Generic[ResultType]):
    def __init__(
        self,
        content: ResultType,
        status_code: int = 200,
        headers: Optional[Mapping[str, str]] = None,
        media_type: Optional[str] = None,
        background: Optional[BackgroundTask] = None,
    ) -> None:
        super().__init__(content, status_code, headers, media_type, background)

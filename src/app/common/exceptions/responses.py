from dataclasses import dataclass
from typing import Generic, TypeVar

TError = TypeVar("TError")


@dataclass(frozen=True)
class ErrorResponse(Generic[TError]):
    status: int = 500
    error: TError | str = "Unknown error occurred"

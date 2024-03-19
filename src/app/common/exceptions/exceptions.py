from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppException(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An app error occurred"


class ApplicationException(AppException):
    @property
    def title(self) -> str:
        return "An application error occurred"


class NotFoundError(ApplicationException):
    @property
    def title(self) -> str:
        return "An application error occurred"

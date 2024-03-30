from dataclasses import dataclass


@dataclass(eq=False)
class AppException(Exception):
    @property
    def title(self) -> str:
        return "An app error occurred"


class ApplicationException(AppException):
    @property
    def title(self) -> str:
        return "An application error occurred"

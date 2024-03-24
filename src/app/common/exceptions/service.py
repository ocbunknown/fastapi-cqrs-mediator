from dataclasses import dataclass
from typing import ClassVar, Optional

from src.app.common.exceptions import ApplicationException


@dataclass(eq=False)
class AlreadyExistsError(ApplicationException):
    status: ClassVar[int] = 409

    user_id: Optional[int] = None
    message: Optional[str] = None

    @property
    def title(self) -> str:
        if self.message is not None:
            return self.message

        if self.user_id is not None:
            return f"A user with the '{self.user_id}' user_id already exists"

        return "User already exists"


@dataclass(eq=False)
class NotFoundError(ApplicationException):
    status: ClassVar[int] = 404

    user_id: Optional[int] = None
    message: Optional[str] = None

    @property
    def title(self) -> str:
        if self.message is not None:
            return self.message

        if self.user_id is not None:
            return f"A user with the id '{self.user_id}' not found"

        return "User not found"


class InvalidParamsError(ApplicationException):
    status: ClassVar[int] = 400

    @property
    def title(self) -> str:
        return "At least 1 parameter must be provided"

from dataclasses import dataclass
from typing import Optional

from src.app.common.exceptions import ApplicationException


@dataclass(eq=False)
class AlreadyExistsError(ApplicationException):
    user_id: Optional[int] = None
    message: Optional[str] = None

    @property
    def title(self) -> str:
        if self.message is not None:
            return self.message

        if self.user_id is not None:
            return f'A user with the "{self.user_id}" user_id already exists'

        return "A user with this user_id already exists"

@dataclass(eq=False)
class NotFoundError(ApplicationException):
    user_id: Optional[int] = None
    message: Optional[str] = None

    @property
    def title(self) -> str:
        if self.message is not None:
            return self.message

        if self.user_id is not None:
            return f'A user with the id "{self.user_id}" not found'

        return "User not found"


class InvalidParamsError(ApplicationException):
    @property
    def title(self) -> str:
        return "At least 1 parameter must be provided"

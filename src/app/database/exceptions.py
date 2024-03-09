from typing import Any


class DatabaseError(Exception):
    pass


class CommitError(DatabaseError):
    pass


class RollbackError(DatabaseError):
    pass


class InvalidParamsError(Exception):
    def __init__(
        self,
        message: Any,
        **kwargs: Any,
    ) -> None:
        self.__dict__.update(kwargs)
        Exception.__init__(message)

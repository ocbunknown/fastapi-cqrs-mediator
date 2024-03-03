from typing import Any


class NotFoundError(Exception):
    def __init__(self, message: str, status_code: int, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)
        Exception.__init__(self, message, status_code)

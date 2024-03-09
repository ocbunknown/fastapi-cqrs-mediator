from abc import abstractmethod
from typing import Protocol


class PasswordHelperProtocol(Protocol):
    @abstractmethod
    def verify_and_update(
        self, plain_password: str, hashed_password: str
    ) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def hash(self, password: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError

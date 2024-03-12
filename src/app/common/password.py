from typing import Optional

from passlib import pwd
from passlib.context import CryptContext

from src.app.common.interfaces.password import PasswordHelperProtocol


class PasswordHelper(PasswordHelperProtocol):
    def __init__(self, context: Optional[CryptContext] = None) -> None:
        if context is None:
            self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        else:
            self.context = context

    def verify_and_update(
        self, plain_password: str, hashed_password: str
    ) -> tuple[bool, str]:
        return self.context.verify_and_update(plain_password, hashed_password)  # type: ignore

    def hash(self, password: str) -> str:
        return self.context.hash(password)

    def generate(self) -> str:
        return pwd.genword()  # type: ignore

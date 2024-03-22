from typing import Final

from passlib.context import CryptContext

_crypto: Final[CryptContext] = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(
    plain_password: str, hashed_password: str
) -> tuple[bool, str | None]:
    return _crypto.verify_and_update(plain_password, hashed_password)


def bcrypt_hash(password: str) -> str:
    return _crypto.hash(password)

import os
from pathlib import Path
from typing import (
    Optional,
    Type,
    TypeAlias,
    Union,
)

from pydantic_settings import BaseSettings, SettingsConfigDict

_StrPath: TypeAlias = Union[os.PathLike[str], str, Path]


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    POSTGRES_URI: str
    POSTGRES_DB: str
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[int] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    ECHO: Optional[bool] = False
    WORKERS: Optional[int] = 4

    @property
    def url(self) -> str:
        return self.POSTGRES_URI.format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST,
            self.POSTGRES_PORT,
            self.POSTGRES_DB,
        )

class Settings(BaseSettings):
    db: DatabaseSettings

    @staticmethod
    def root_dir() -> Path:
        return Path(__file__).resolve().parent.parent.parent

    @classmethod
    def path(
        cls: Type["Settings"], *paths: _StrPath, base_path: Optional[_StrPath] = None
    ) -> _StrPath:
        if base_path is None:
            base_path = cls.root_dir()

        return Path(base_path, *paths)


def load_settings(
    database_settings: Optional[DatabaseSettings] = None,
) -> Settings:
    return Settings(
        db=database_settings or DatabaseSettings(),  # type: ignore[call-arg]
    )

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
        env_prefix="DB_",
        extra="ignore",
    )

    uri: str
    name: str
    host: Optional[str] = None
    port: Optional[int] = None
    user: Optional[str] = None
    password: Optional[str] = None
    echo: Optional[bool] = False
    future: Optional[bool] = True

    @property
    def url(self) -> str:
        return self.uri.format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.name,
        )

class Gunicorn(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    WORKERS: Optional[int] = None
    LEVEL: Optional[str] = None
    HOST: Optional[str] = None
    BACKEND_PORT: Optional[int] = None
    SECRET_KEY: Optional[str] = None
    BACKEND_CORS_ORIGINS: Optional[list[str]] = []


class Settings(BaseSettings):
    db: DatabaseSettings
    gunicorn: Gunicorn

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
    gunicorn: Optional[Gunicorn] = None,
) -> Settings:
    return Settings(
        db=database_settings or DatabaseSettings(),  # type: ignore[call-arg]
        gunicorn=gunicorn or Gunicorn(),
    )

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    DB_PORT_TEST: Optional[str] = None
    DB_HOST_TEST: Optional[str] = None
    DB_USER_TEST: Optional[str] = None
    DB_PASS_TEST: Optional[str] = None
    DB_NAME_TEST: Optional[str] = None
    DB_PORT: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_USER: Optional[str] = None
    DB_PASS: Optional[str] = None
    DB_NAME: Optional[str] = None
    ECHO: bool = True

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

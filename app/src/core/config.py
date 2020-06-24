import secrets
from typing import Any, Dict, Optional

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "woden-bot"
    # SERVER_HOST: AnyHttpUrl = AnyHttpUrl("localhost")
    USERS_OPEN_REGISTRATION: bool = True
    PROJECT_NAME: str = "Woden Bot"
    SENTRY_DSN: Optional[HttpUrl] = None
    # POSTGRES_SERVER: str = "postgres-compose"
    POSTGRES_SERVER: str = "localhost"
    # POSTGRES_USER: str = "postgres"
    POSTGRES_USER: str = "postgres"
    # POSTGRES_PASSWORD: str = "Postgres2020!"
    # POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "work"
    POSTGRES_PORT: str = "15432"

    # Connection URI Format: dialect+driver://username:password@host:port/database
    DATABASE_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB)

    class Config:
        case_sensitive = True


settings = Settings()

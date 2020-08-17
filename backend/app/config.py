# backend/app/config.py

import logging

from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator
from functools import lru_cache


log = logging.getLogger(__name__)


class Settings(BaseSettings):
    ALLOWED_HOSTS: str
    SECRET_KEY: str

    # Postgres configurations
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    DATABASE_URL: Optional[PostgresDsn] = None

    @validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            port=values.get("POSTGRES_PORT"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_DB'), ''}",
        )

        class Config:
            case_sensitive = True

            # If you want to read environment variables from a .env
            # file instead un-comment the below line and create the
            # .env file at the root of the project.

            env_file = ".env"


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment")
    return Settings()

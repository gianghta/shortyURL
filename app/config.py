from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


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
            path=f"/{values.get('POSTGRES_DB') or  ''}",
        )

        class Config:
            case_sensitive = True
            env_file = ".env"


settings = Settings()

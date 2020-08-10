from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret


config = Config(".env")


ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings)
SECRET_KEY = config("SECRET_KEY", cast=Secret)
POSTGRES_USER = config("POSTGRES_USER", cast=Secret)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_PORT = config("POSTGRES_PORT", cast=Secret)
POSTGRES_DB = config("POSTGRES_DB", cast=Secret)
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:{POSTGRES_PORT}/{POSTGRES_DB}"

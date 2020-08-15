from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from config import settings


engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session.
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

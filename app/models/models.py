from time import time
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from app.db.database import Base


def unix_time():
    return int(time())

class Url(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    encoded_url = Column(String)
    actual_url = Column(String)
    created_at = Column(Integer, default=unix_time)
    updated_at = Column(Integer, onupdate=unix_time)
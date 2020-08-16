from time import time
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.types import Date
from hashlib import md5

from . import schemas
from app.db.session import Base


def unix_time():
    return int(time())


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True, autoincrement=True)
    encoded_url = Column(String)
    actual_url = Column(String)
    created_at = Column(Integer, default=unix_time)
    updated_at = Column(Integer, onupdate=unix_time)

    @classmethod
    def get(cls, db: Session, url: schemas.EncodedUrlSchema):
        return db.query(Url).filter(Url.encoded_url == url.encoded_url).first()

    @classmethod
    def get_all_url(cls, db: Session, url: schemas.EncodedUrlSchema):
        return db.query(Url).filter(Url.encoded_url == url.encoded_url).all()

    @classmethod
    def post(cls, db: Session, url: schemas.ActualUrlSchema):
        # hashing url
        query = db.query(Url).filter(Url.actual_url == url.actual_url).first()

        if not query:
            processed_url = url.actual_url.replace("https://", "")
            processed_url = processed_url.replace("http://", "")
            hashObject = md5(processed_url.encode("utf-8"))
            shrinkedURL = hashObject.hexdigest()[:8]

            new_url = Url(actual_url=url.actual_url, encoded_url=shrinkedURL)
            db.add(new_url)
            db.commit()
            db.refresh(new_url)
            return new_url
        else:
            return query

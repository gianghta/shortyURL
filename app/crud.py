from sqlalchemy.orm import Session

import models, schemas


def get_actual_url(db: Session, encoded_url: str):
    return db.query(models.Url).filter(models.Url.encoded_url == encoded_url).actual_url


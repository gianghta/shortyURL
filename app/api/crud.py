from sqlalchemy.orm import Session
from hashlib import md5

from app.models import models, schemas


def post(db: Session, url: schemas.UrlPayloadSchema):
    # hashing url
    hashObject = md5(url.actual_url)
    shrinkedURL = hashObject.hexdigest()[:8]
    
    new_url = models.Url(actual_url=url.actual_url, encoded_url=shrinkedURL)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url
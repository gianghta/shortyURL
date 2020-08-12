from sqlalchemy.orm import Session
from hashlib import md5

from models import models, schemas


def get(db: Session, url: schemas.EncodedUrlSchema):
    return db.query(models.Url).filter(models.Url.encoded_url == url).first()

def post(db: Session, url: schemas.ActualUrlSchema):
    # hashing url
    processed_url = url.actual_url.replace('https://', '')
    processed_url = processed_url.replace('http://', '')
    hashObject = md5(processed_url.encode('utf-8'))
    shrinkedURL = hashObject.hexdigest()[:8]

    new_url = models.Url(actual_url=url.actual_url, encoded_url=shrinkedURL)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.models import Url
from app.db.schemas import ActualUrlSchema, EncodedUrlSchema
from app.db.session import get_db


router = APIRouter()


@router.get("/")
def hello_world():
    return {"Hello": "World"}


@router.get("/{encoded_url}/", response_model=ActualUrlSchema, status_code=200)
def get_actual_url(encoded_url: str, db: Session = Depends(get_db)) -> ActualUrlSchema:
    return_url = Url.get(db, encoded_url)

    response_object = {"id": return_url.id, "actual_url": return_url.actual_url}

    return response_object


@router.post("/", response_model=EncodedUrlSchema, status_code=201)
def create_encoded_url(
    payload: ActualUrlSchema, db: Session = Depends(get_db)
) -> EncodedUrlSchema:
    new_url = Url.post(db, payload)

    response_object = {
        "id": new_url.id,
        "encoded_url": "http://localhost:8000/{}".format(new_url.encoded_url),
    }

    return response_object


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api import crud
from models.schemas import ActualUrlSchema, EncodedUrlSchema
from main import get_db


router = APIRouter()

@router.get("/")
def hello_world():
    return {"Hello": "World"}

@router.get("/{encoded_url}/", response_model=ActualUrlSchema, status_code=200)
def get_actual_url(encoded_url: str, db: Session = Depends(get_db)) -> ActualUrlSchema:
    return_url = crud.get(db, encoded_url)

    response_object = {
        "id": return_url.id,
        "actual_url": return_url.actual_url
    }

    return response_object

@router.post("/", response_model=EncodedUrlSchema, status_code=201)
def create_encoded_url(payload: ActualUrlSchema, db: Session = Depends(get_db)) -> EncodedUrlSchema:
    new_url = crud.post(db, payload)

    response_object = {
        "id": new_url.id,
        "encoded_url": new_url.encoded_url
    }

    return response_object

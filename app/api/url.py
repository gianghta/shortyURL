from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api import crud
from models.schemas import UrlPayloadSchema, UrlResponseSchema
from main import get_db


router = APIRouter()

@router.get("/")
async def hello_world():
    return {"Hello": "World"}

@router.post("/", response_model=UrlResponseSchema, status_code=201)
async def create_encoded_url(payload: UrlPayloadSchema, db: Session = Depends(get_db)) -> UrlResponseSchema:
    new_url = await crud.post(db, payload)

    response_object = {
        "id": new_url.id,
        "encoded_url": new_url.encoded_url
    }

    return response_object

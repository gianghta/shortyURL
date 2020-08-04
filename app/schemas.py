from datetime import date
from pydantic import BaseModel


class Url(BaseModel):
    id: int
    encoded_url: str
    actual_url: str
    created_at: int
    updated_at: int

    class Config:
        orm_mod = True
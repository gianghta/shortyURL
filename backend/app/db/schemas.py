from pydantic import BaseModel


class ActualUrlSchema(BaseModel):
    actual_url: str

    class Config:
        orm_mode = True

class EncodedUrlSchema(BaseModel):
    encoded_url: str

    class Config:
        orm_mode = True
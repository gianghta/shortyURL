from pydantic import BaseModel


class UrlPayloadSchema(BaseModel):
    actual_url: str

    class Config:
        orm_mod = True

class UrlResponseSchema(BaseModel):
    encoded_url: str

    class Config:
        orm_mod = True
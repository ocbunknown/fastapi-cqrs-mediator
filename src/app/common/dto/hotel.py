from pydantic import BaseModel, Field


class Hotel(BaseModel):
    addres: str
    name: str
    stars: int = Field(le=1, ge=5)

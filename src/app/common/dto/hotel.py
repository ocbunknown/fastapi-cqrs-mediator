from pydantic import BaseModel, Field


class HotelDTO(BaseModel):
    addres: str
    name: str
    stars: int = Field(le=1, ge=5)

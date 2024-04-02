# models.py

from pydantic import BaseModel, Field

class Vehicle(BaseModel):
    id: int
    make: str = Field(..., pattern="^[a-zA-Z0-9 ]+$")
    model: str = Field(..., pattern="^[a-zA-Z0-9 ]+$")
    price: float = Field(..., ge=0)

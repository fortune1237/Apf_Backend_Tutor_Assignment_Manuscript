from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class TicketType(str, Enum):
    regular = "regular"
    vip = "vip"
    premium = "premium"

class Event(BaseModel):
    name: str
    date: str
    location: str

class Attendee(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(..., gt=0)

class BookingRequest(BaseModel):
    event: Event
    attendee: Attendee
    ticket_type: TicketType

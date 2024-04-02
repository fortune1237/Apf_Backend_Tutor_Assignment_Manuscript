from fastapi import APIRouter, HTTPException
from models import BookingRequest, TicketType

router = APIRouter()

@router.post("/book_event/")
async def book_event(booking_request: BookingRequest):
    # Validate attendee's age
    if booking_request.attendee.age < 18:
        raise HTTPException(status_code=400, detail="Attendee must be at least 18 years old")

    # Check if ticket type is valid
    if booking_request.ticket_type not in TicketType:
        raise HTTPException(status_code=400, detail="Invalid ticket type")

    # Perform booking logic (e.g., save to database)
    # For demonstration purposes, just return the booking details
    return {
        "message": "Booking confirmed",
        "event_details": booking_request.event.dict(),
        "attendee_details": booking_request.attendee.dict(),
        "ticket_type": booking_request.ticket_type.value
    }

from fastapi.testclient import TestClient
from main import app
from models import Event, Attendee, TicketType

client = TestClient(app)

def test_book_event_success():
    # Define a valid booking request
    booking_data = {
        "event": {
            "name": "Test Event",
            "date": "2024-04-02",
            "location": "Test Location"
        },
        "attendee": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25
        },
        "ticket_type": "regular"
    }

    # Make a request to book an event
    response = client.post("/book_event/", json=booking_data)

    # Assert that the request was successful (status code 200)
    assert response.status_code == 200

    # Assert response data
    data = response.json()
    assert data["message"] == "Booking confirmed"
    assert data["event_details"] == booking_data["event"]
    assert data["attendee_details"] == booking_data["attendee"]
    assert data["ticket_type"] == booking_data["ticket_type"]

def test_book_event_invalid_age():
    # Define a booking request with invalid attendee age
    booking_data = {
        "event": {
            "name": "Test Event",
            "date": "2024-04-02",
            "location": "Test Location"
        },
        "attendee": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 17  # Invalid age
        },
        "ticket_type": "regular"
    }

    # Make a request to book an event with invalid age
    response = client.post("/book_event/", json=booking_data)

    # Assert that the request was unsuccessful (status code 400)
    assert response.status_code == 400

def test_book_event_invalid_ticket_type():
    # Define a booking request with invalid ticket type
    booking_data = {
        "event": {
            "name": "Test Event",
            "date": "2024-04-02",
            "location": "Test Location"
        },
        "attendee": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25
        },
        "ticket_type": "invalid_ticket_type"  # Invalid ticket type
    }

    # Make a request to book an event with invalid ticket type
    response = client.post("/book_event/", json=booking_data)

    # Assert that the request was unsuccessful (status code 400)
    assert response.status_code == 422
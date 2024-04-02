from fastapi.testclient import TestClient
from main import app
from models import Booking, ContactDetails, FlightDetails

client = TestClient(app)

def test_create_booking_success():
    # Define a valid booking request
    booking_data = {
        "contact_details": {
            "name": "John Doe",
            "age": 25,
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "next_of_kin": "Jane Doe"
        },
        "flight_details": {
            "origin": "Lagos",
            "destination": "Abuja",
            "flight_date": "2024-04-02"
        },
        "seat_pref": "A1"
    }

    # Make a request to create a booking
    response = client.post("/booking/", json=booking_data)

    # Assert that the request was successful (status code 201)
    assert response.status_code == 201

    # Assert response data
    data = response.json()["data"]
    assert data["customer_name"] == booking_data["contact_details"]["name"]
    assert data["customer_age"] == booking_data["contact_details"]["age"]
    assert data["customer_email"] == booking_data["contact_details"]["email"]
    assert data["customer_phone"] == booking_data["contact_details"]["phone"]
    assert data["flight_origin"] == booking_data["flight_details"]["origin"]
    assert data["flight_destination"] == booking_data["flight_details"]["destination"]
    assert data["flight_date"] == booking_data["flight_details"]["flight_date"]
    assert data["seat_preference"] == booking_data["seat_pref"]


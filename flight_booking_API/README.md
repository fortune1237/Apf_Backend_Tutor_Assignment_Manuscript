# Flight Booking API

The Flight Booking API facilitates booking flights by providing endpoints for passenger information, flight details, and seat preferences.

## Features

- **Route**: Create a FastAPI route (`POST /book_flight`) for booking flights.
- **Request Body Parameters**: Utilize request body parameters for passenger information, flight details, and seat preferences.
    - **Passenger Information**:
        - `name`: The name of the passenger.
        - `age`: The age of the passenger.
        - `contact_details`: Contact details of the passenger.
    - **Flight Details**:
        - `origin`: The origin airport of the flight.
        - `destination`: The destination airport of the flight.
        - `date`: The date of the flight.
    - **Seat Preferences**: Preferences for seat selection.
- **Validation**:
    - **Passenger Names and Contact Details**: Implement string validation to ensure that passenger names and contact details are valid strings.
    - **Passenger Age**: Apply numeric validation to ensure that the passenger age is a valid number.
    - **Flight-related Fields**: Implement numeric validation for flight-related fields such as origin and destination.
    - **Seat Preferences**: Ensure that seat preferences are within valid options.
- **Booking Process**: Simulate the flight booking process within the route and return booking confirmation upon successful booking.
- **Testing**: Test the API with various combinations of valid and invalid input data to ensure that the booking process works as expected.

## Usage

To use the Flight Booking API, send a POST request to the `/book_flight` endpoint with the required passenger information, flight details, and seat preferences in the request body:

```http
POST /book_flight
Content-Type: application/json

{
  "passenger": {
    "name": "John Doe",
    "age": 30,
    "contact_details": "john.doe@example.com"
  },
  "flight": {
    "origin": "JFK",
    "destination": "LAX",
    "date": "2024-04-15"
  },
  "seat_preference": "Window"
}

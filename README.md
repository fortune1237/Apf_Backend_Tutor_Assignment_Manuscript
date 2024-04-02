# User Registration API

This API provides functionality for user registration. It includes validation for username, email, and password.

## Features
- **Route**: Create a FastAPI route for user registration.
- **Request Body Parameters**: Utilize request body parameters for username, email, and password.
- **Validation**: Implement string validation for username and email. Ensure password meets certain complexity requirements.
- **Error Handling**: Return appropriate error messages for invalid inputs.
- **Testing**: Simulate registration process with FastAPI TestClient.

---

# Product Search API

This API facilitates searching for products based on various criteria such as name, category, and price range.

## Features
- **Endpoint**: Develop a FastAPI endpoint for searching products.
- **Query Parameters**: Accept query parameters for product name, category, and price range.
- **Validation**: Implement string validation for product name and category. Apply numeric validation for price range parameters.
- **Results**: Return a list of products matching the search criteria.
- **Testing**: Test the API with various combinations of query parameters.

---

# Payment Processing API

This API enables processing payments securely. It includes validation for payment amount, card details, and expiration date.

## Features
- **Route**: Build a FastAPI route for processing payments.
- **Request Body Parameters**: Utilize request body parameters for payment amount, card number, expiration date, and CVV.
- **Validation**: Implement numeric validation for payment amount and card-related fields. Validate expiration date format and ensure it's not expired.
- **Processing Logic**: Simulate payment processing logic within the route.
- **Testing**: Test the API with valid and invalid payment data.

---

# Vehicle Inventory API

This API manages vehicle inventory and provides functionality for filtering vehicles by make, model, and price range.

## Features
- **Endpoint**: Develop a FastAPI endpoint for managing vehicle inventory.
- **Parameters**: Use path parameters for vehicle ID and query parameters for filtering.
- **Validation**: Apply numeric validation for vehicle ID and price range. Implement string validation for make and model parameters.
- **Results**: Return details of a specific vehicle identified by ID or a list of vehicles based on query parameters.
- **Testing**: Test the API with various combinations of parameters.

---

# Flight Booking API

This API allows users to book flights with validation for passenger information, flight details, and seat preferences.

## Features
- **Route**: Create a FastAPI route for booking flights.
- **Request Body Parameters**: Utilize request body parameters for passenger and flight details.
- **Validation**: Implement string validation for passenger names and contact details. Apply numeric validation for passenger age and flight-related fields. Ensure seat preferences are within valid options.
- **Booking Process**: Simulate flight booking process and return booking confirmation.
- **Testing**: Test the API with different combinations of inputs.

---

# Event Booking API

This API facilitates booking events such as concerts and workshops with validation for attendee information, event details, and ticket type.

## Features
- **Endpoint**: Build a FastAPI endpoint for booking events.
- **Request Body Parameters**: Utilize request body parameters for attendee and event details.
- **Validation**: Implement string validation for attendee details and event name. Apply numeric validation for attendee age. Validate ticket type against available options.
- **Confirmation**: Return booking confirmation with event details.
- **Testing**: Test the API with various scenarios, including full and partial bookings.

 

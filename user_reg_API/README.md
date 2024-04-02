# User Registration API

The User Registration API allows users to register by providing their username, email, and password. It ensures that the provided information meets certain validation criteria before registering the user.

## Features

- **Route**: Create a FastAPI route (`POST /register`) for user registration.
- **Request Body Parameters**: Utilize request body parameters for username, email, and password.
    - `username`: The desired username for the user account.
    - `email`: The email address associated with the user account.
    - `password`: The password for the user account.
- **Validation**:
    - **Username**: Implement string validation to ensure that the username meets the following criteria:
        - Must be alphanumeric with underscores allowed.
        - Must be between 3 and 20 characters long.
    - **Email**: Implement string validation to ensure that the email address is in a valid format.
    - **Password**: Ensure that the password meets certain complexity requirements, such as:
        - Minimum length of 8 characters.
        - Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **Error Handling**: Return appropriate error messages for invalid inputs, such as:
    - Invalid username format.
    - Invalid email format.
    - Password does not meet complexity requirements.
- **Testing**: Simulate the registration process with FastAPI TestClient to ensure that the API behaves as expected under various scenarios.

## Usage

To use the User Registration API, send a POST request to the `/register` endpoint with the following JSON payload:

```json
{
  "username": "example_user",
  "email": "user@example.com",
  "password": "SecurePassword123!"
}
```
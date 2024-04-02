# Payment Processing API

The Payment Processing API enables users to securely process payments by providing payment amount, card details, and expiration date.

## Features

- **Route**: Build a FastAPI route (`POST /process_payment`) for processing payments.
- **Request Body Parameters**: Utilize request body parameters for payment amount, card number, expiration date, and CVV.
    - `amount`: The amount to be charged for the payment.
    - `card_number`: The credit/debit card number for the payment.
    - `expiration_date`: The expiration date of the card.
    - `cvv`: The Card Verification Value for the card.
- **Validation**:
    - **Payment Amount**: Implement numeric validation to ensure that the payment amount is a valid number.
    - **Card-related Fields**: Apply numeric validation to ensure that the card number and CVV are valid numbers.
    - **Expiration Date Format**: Validate expiration date format to ensure it follows the MM/YYYY format.
    - **Expiration Date Validity**: Ensure that the expiration date is not expired.
- **Payment Processing Logic**: Simulate payment processing logic within the route, including validation and authentication.
- **Testing**: Test the API with both valid and invalid payment data to ensure that it behaves correctly under various scenarios.

## Usage

To use the Payment Processing API, send a POST request to the `/process_payment` endpoint with the required payment details in the request body:

```http
POST /process_payment
Content-Type: application/json

{
  "amount": 50.00,
  "card_number": "1234567890123456",
  "expiration_date": "12/2025",
  "cvv": "123"
}
```
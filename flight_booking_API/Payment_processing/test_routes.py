from fastapi.testclient import TestClient
from main import app
from models import PaymentRequest

client = TestClient(app)

def test_process_payment_success():
    # Define a valid payment request
    payment_data = {
        "amount": 2333,
        "card_number": "1234567890123456",
        "expiration_date": "2024-10-03",
        "cvv": "111"
    }

    # Make a request to process payment
    response = client.post("/booking/process_payment/", json=payment_data)

    # Assert that the request was successful (status code 201)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Assert response message
    assert response.json() == {
        "payment": {
            "amount": 2333,
            "card_number": "1234567890123456",
            "expiration_date": "2024-10-03T00:00:00",
            "cvv": "111"
        }
    }

# Additional tests can be added as needed

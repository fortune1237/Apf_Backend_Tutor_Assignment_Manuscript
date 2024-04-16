from fastapi.testclient import TestClient
from vehicle_inventory_API.main import app



client = TestClient(app)

def test_register_user():
    # Weak password
    response = client.post("/register", json={"username": "username", "email": "user@example.com", "password": "weakpass"})
    assert response.status_code == 422

    # Valid registration
    response = client.post("/register", json={"username": "username", "email": "user@example.com", "password": "StrongPassword123!"})
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

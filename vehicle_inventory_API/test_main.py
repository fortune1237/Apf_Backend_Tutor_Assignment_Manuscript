# test_routes.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_vehicle_by_id():
    response = client.get("/vehicles/1")
    assert response.status_code == 200
    assert response.json()["make"] == "Toyota"

def test_get_vehicles():
    response = client.get("/vehicles/?make=Toyota&max_price=26000")
    assert response.status_code == 200
    assert len(response.json()) == 1

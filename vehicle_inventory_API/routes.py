# routes.py

from fastapi import APIRouter, Query, Path
from models import Vehicle

router = APIRouter()

# Example data - Vehicle inventory
vehicle_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "price": 25000},
    {"id": 2, "make": "Honda", "model": "Civic", "price": 22000},
    {"id": 3, "make": "Ford", "model": "F-150", "price": 35000},
    {"id": 4, "make": "Chevrolet", "model": "Silverado", "price": 38000},
]

@router.get("/{vehicle_id}")
def get_vehicle_by_id(vehicle_id: int = Path(..., title="The ID of the vehicle to retrieve")):
    for vehicle in vehicle_inventory:
        if vehicle["id"] == vehicle_id:
            return vehicle
    return {"error": "Vehicle not found"}

@router.get("/")
def get_vehicles(
    make: str = Query(None, title="Make of the vehicle"),
    model: str = Query(None, title="Model of the vehicle"),
    min_price: float = Query(None, title="Minimum price of the vehicle"),
    max_price: float = Query(None, title="Maximum price of the vehicle")
):
    filtered_vehicles = vehicle_inventory
    if make:
        filtered_vehicles = [vehicle for vehicle in filtered_vehicles if vehicle["make"] == make]
    if model:
        filtered_vehicles = [vehicle for vehicle in filtered_vehicles if vehicle["model"] == model]
    if min_price is not None:
        filtered_vehicles = [vehicle for vehicle in filtered_vehicles if vehicle["price"] >= min_price]
    if max_price is not None:
        filtered_vehicles = [vehicle for vehicle in filtered_vehicles if vehicle["price"] <= max_price]
    return filtered_vehicles

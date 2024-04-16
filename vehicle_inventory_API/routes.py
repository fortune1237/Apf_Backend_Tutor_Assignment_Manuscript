# routes.py

from fastapi import APIRouter, Query, Path
from models import Vehicle

router = APIRouter()

# Example data - Vehicle inventory
vehicle_inventory = [
  {
    "id": 1,
    "make": "Toyota",
    "model": "Camry",
    "price": 25000
  },
  {
    "id": 2,
    "make": "Honda",
    "model": "Civic",
    "price": 22000
  },
  {
    "id": 3,
    "make": "Ford",
    "model": "F-150",
    "price": 35000
  },
  {
    "id": 4,
    "make": "Chevrolet",
    "model": "Silverado",
    "price": 38000
  },
  {
    "id": 5,
    "make": "Nissan",
    "model": "Altima",
    "price": 27000
  },
  {
    "id": 6,
    "make": "BMW",
    "model": "3 Series",
    "price": 45000
  },
  {
    "id": 7,
    "make": "Mercedes-Benz",
    "model": "C-Class",
    "price": 50000
  },
  {
    "id": 8,
    "make": "Audi",
    "model": "A4",
    "price": 42000
  },
  {
    "id": 9,
    "make": "Lexus",
    "model": "RX",
    "price": 52000
  },
  {
    "id": 10,
    "make": "Subaru",
    "model": "Outback",
    "price": 33000
  },
  {
    "id": 11,
    "make": "Jeep",
    "model": "Wrangler",
    "price": 34000
  },
  {
    "id": 12,
    "make": "Tesla",
    "model": "Model 3",
    "price": 45000
  },
  {
    "id": 13,
    "make": "Kia",
    "model": "Optima",
    "price": 25000
  },
  {
    "id": 14,
    "make": "Hyundai",
    "model": "Sonata",
    "price": 26000
  },
  {
    "id": 15,
    "make": "Mazda",
    "model": "CX-5",
    "price": 29000
  },
  {
    "id": 16,
    "make": "Volvo",
    "model": "XC90",
    "price": 62000
  },
  {
    "id": 17,
    "make": "Volkswagen",
    "model": "Jetta",
    "price": 23000
  },
  {
    "id": 18,
    "make": "Porsche",
    "model": "911",
    "price": 115000
  },
  {
    "id": 19,
    "make": "Land Rover",
    "model": "Range Rover",
    "price": 95000
  },
  {
    "id": 20,
    "make": "Ferrari",
    "model": "488 GTB",
    "price": 350000
  },
  {
    "id": 21,
    "make": "Lamborghini",
    "model": "Huracan",
    "price": 300000
  },
  {
    "id": 22,
    "make": "Maserati",
    "model": "Ghibli",
    "price": 76000
  },
  {
    "id": 23,
    "make": "Jaguar",
    "model": "F-Type",
    "price": 68000
  },
  {
    "id": 24,
    "make": "Acura",
    "model": "MDX",
    "price": 45000
  },
  {
    "id": 25,
    "make": "Buick",
    "model": "Encore",
    "price": 28000
  },
  {
    "id": 26,
    "make": "Cadillac",
    "model": "Escalade",
    "price": 85000
  },
  {
    "id": 27,
    "make": "Chrysler",
    "model": "300",
    "price": 38000
  },
  {
    "id": 28,
    "make": "Dodge",
    "model": "Challenger",
    "price": 29000
  },
  {
    "id": 29,
    "make": "GMC",
    "model": "Yukon",
    "price": 65000
  },
  {
    "id": 30,
    "make": "Infiniti",
    "model": "Q50",
    "price": 40000
  },
  {
    "id": 31,
    "make": "Lincoln",
    "model": "Navigator",
    "price": 75000
  },
  {
    "id": 32,
    "make": "Mini",
    "model": "Cooper",
    "price": 32000
  },
  {
    "id": 33,
    "make": "Ram",
    "model": "1500",
    "price": 40000
  },
  {
    "id": 34,
    "make": "Jeep",
    "model": "Grand Cherokee",
    "price": 42000
  },
  {
    "id": 35,
    "make": "Subaru",
    "model": "Forester",
    "price": 29000
  },
  {
    "id": 36,
    "make": "Toyota",
    "model": "RAV4",
    "price": 28000
  },
  {
    "id": 37,
    "make": "Volvo",
    "model": "S60",
    "price": 45000
  },
  {
    "id": 38,
    "make": "Audi",
    "model": "Q5",
    "price": 49000
  },
  {
    "id": 39,
    "make": "BMW",
    "model": "X5",
    "price": 59000
  },
  {
    "id": 40,
    "make": "Cadillac",
    "model": "XT5",
    "price": 48000
  },
  {
    "id": 41,
    "make": "Chevrolet",
    "model": "Equinox",
    "price": 30000
  },
  {
    "id": 42,
    "make": "Dodge",
    "model": "Durango",
    "price": 43000
  },
  {
    "id": 43,
    "make": "Ford",
    "model": "Escape",
    "price": 31000
  },
  {
    "id": 44,
    "make": "GMC",
    "model": "Terrain",
    "price": 32000
  },
  {
    "id": 45,
    "make": "Honda",
    "model": "Accord",
    "price": 28000
  },
  {
    "id": 46,
    "make": "Hyundai",
    "model": "Tucson",
    "price": 26000
  },
  {
    "id": 47,
    "make": "Infiniti",
    "model": "QX60",
    "price": 46000
  },
  {
    "id": 48,
    "make": "Jeep",
    "model": "Cherokee",
    "price": 32000
  },
  {
    "id": 49,
    "make": "Kia",
    "model": "Sorento",
    "price": 30000
  },
  {
    "id": 50,
    "make": "Lexus",
    "model": "ES",
    "price": 42000
  }
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

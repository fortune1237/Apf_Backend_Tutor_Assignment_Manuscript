# Vehicle Inventory API

The Vehicle Inventory API manages vehicle inventory and provides functionality for filtering vehicles by make, model, and price range.

## Features

- **Endpoint**: Develop a FastAPI endpoint (`GET /vehicles/{vehicle_id}`) for managing vehicle inventory.
- **Path Parameters**: Use path parameters for vehicle ID to retrieve details of a specific vehicle.
    - `vehicle_id`: The unique identifier of the vehicle.
- **Query Parameters**: Utilize query parameters for filtering vehicles by make, model, and price range.
    - `make`: Filter vehicles by make.
    - `model`: Filter vehicles by model.
    - `min_price` and `max_price`: Define a price range for vehicles.
- **Validation**:
    - **Vehicle ID**: Apply numeric validation to ensure that the vehicle ID is a valid number.
    - **Price Range Parameters**: Implement numeric validation to ensure that the price range parameters are valid numbers.
    - **Make and Model**: Implement string validation to ensure that the make and model parameters are valid strings.
- **Results**: Return details of a specific vehicle identified by ID or a list of vehicles based on the query parameters provided by the user.
- **Testing**: Test the API with various combinations of path and query parameters to ensure that the filtering functionality works as expected.

## Usage

To use the Vehicle Inventory API, send a GET request to the `/vehicles/{vehicle_id}` endpoint to retrieve details of a specific vehicle by its ID. Alternatively, use query parameters to filter vehicles based on make, model, and price range:

```http
GET /vehicles/1234
```
or 

```
GET /vehicles?make=Toyota&model=Camry&min_price=20000&max_price=30000
```
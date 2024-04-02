# Product Search API

The Product Search API allows users to search for products based on various criteria such as product name, category, and price range.

## Features

- **Endpoint**: Develop a FastAPI endpoint (`GET /products`) for searching products.
- **Query Parameters**: Accept query parameters for product name, category, and price range.
    - `name`: Search products by name.
    - `category`: Filter products by category.
    - `min_price` and `max_price`: Define a price range for products.
- **Validation**:
    - **Product Name and Category**: Implement string validation to ensure that the product name and category are valid strings.
    - **Price Range Parameters**: Apply numeric validation to ensure that the price range parameters are valid numbers.
- **Results**: Return a list of products matching the search criteria provided by the user.
- **Testing**: Test the API with various combinations of query parameters to ensure that the search functionality works as expected.

## Usage

To use the Product Search API, send a GET request to the `/products` endpoint with the desired query parameters:

```http
GET /products?name=example_product&category=electronics&min_price=100&max_price=500
```
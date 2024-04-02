from fastapi import APIRouter, Query
from controler.read_product import filter_products

router = APIRouter()

@router.get("/product")
async def read_products(product_name: str = Query(default=None, description = "product_name"),
category: str = Query(default=None, description = "product category" ),
price_range: str = Query(default=None, description = "price range")):
  

# we rturn filtered_products else we return error message "product not found"
  
  product_name = product_name
  category = category
  price_range = price_range

  message = filter_products(product_name, price_range, category)

  return message

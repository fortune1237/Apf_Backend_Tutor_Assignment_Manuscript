from fastapi import HTTPException
import json

products=[]
# file = "product.json"

# with open (file,"r") as f:
# 	data = f.read()
# 	products = json.loads(data)

# def filter_products(product_name, price_range, category):
# 	try:
# 		if not any([product_name, price_range, category]):

# 			return{"products": products}
# 		filtered_products = []
# 		#if price_range:
# 		# range = price_range.split("_")
# 		# proposed_range = range(float(r))
# 		for product in products:
# 			if product_name and product_name.lower() not in product['name'].lower():
# 				continue
# 			if price_range:
# 				min_price, max_price = map(float, price_range.split('_'))
# 			if not min_price <= product ['price'] <= max_price:
# 				continue
# 			if category and category.lower() != product['category'].lower():
# 				continue
# 			filtered_products.append(product)
# 		if not filtered_products:
# 			raise HTTPException(status_code=404, detail="No product found that fits the provided parameters")
		
# 		return{"product": filtered_products}
	
# 	except HTTPException as e:
# 		return{"error": e}


# file = "product.json"

# with open(file, "r") as f:
#     products = json.load(f)

# def filter_products(product_name=None, price_range=None, category=None):
#     filtered_products = []
    
#     for product in products:
#         if product_name and product_name.lower() not in product['name'].lower():
#             continue
        
#         if price_range:
#             try:
#                 min_price, max_price = map(float, price_range.split('_'))
#             except ValueError:
#                 raise HTTPException(status_code=400, detail="Invalid price range format. Please provide min_price_max_price")
                
#             if not min_price <= product['price'] <= max_price:
#                 continue
        
#         if category and category.lower() != product['category'].lower():
#             continue
        
#         filtered_products.append(product)
    
#     if not filtered_products:
#         raise HTTPException(status_code=404, detail="No product found that fits the provided parameters")
    
#     return {"products": filtered_products}



from fastapi import HTTPException
import json

products=[]
file = "product.json"

with open (file,"r") as f:
    data = f.read()
    products = json.loads(data)
 


def filter_products(product_name, price_range, category):
    try:
        if not any([product_name, price_range, category]):
            return {"products":products}
        
        filtered_products = []
        
        # if price_range:

        #     range = price_range.split("-")
        #     proposed_range = range(float(r))
        for product in products:
            if product_name and product_name.lower() not in product['name'].lower():
                continue
            if price_range:
                min_price, max_price = map (float, price_range.split('_'))
                if not  min_price <= product ['price'] <= max_price:
                    continue
            if category and category.lower() != product['category'].lower():
                continue
            filtered_products.append(product)
        if not filtered_products:
            raise HTTPException(status_code=404, detail="no product found for the provided parameter")
        
        return {"product": filtered_products}
    
    except HTTPException as e:
        return {"error": e}
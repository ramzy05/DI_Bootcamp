import json


def retrieve_all_products():
  with open ('products.json') as f:
    return json.load(f)

all_products = retrieve_all_products()
def retrieve_requested_product(product_id):
  with open ('products.json') as f:
    all_products = json.load(f)
  return [product for product in all_products if product['ProductId'] == product_id]

requested_product = retrieve_requested_product('HT-1107')

print(requested_product)
import json


def retrieve_all_products():
  with open ('products.json') as f:
    return list(json.load(f))

all_products = retrieve_all_products()
def retrieve_requested_product(product_id):
  with open ('products.json') as f:
    all_products = json.load(f)
  return [product for product in all_products if product['ProductId'] == product_id][0]

def add_cart(product_id):
  with open ('cart.json') as f:
    cart_item = json.load(f)
  print(cart_item)
    # cart_item.append(retrieve_requested_product(product_id))

  # with open ('cart.json', 'w') as f:
    # json.dump(cart_item,f)

def del_cart(product_id):
  with open ('cart.json') as f:
    cart_item = json.load(f)
  cart_item = [product for product in cart_item if product['ProductId'] != product_id][0]  
  with open ('cart.json', 'w') as f:
    json.dump(cart_item,f)

  with open ('cart.json', 'w') as f:
    f.write(json.dump(cart_item))

if __name__ == '__main__':

  requested_product = retrieve_requested_product('HT-1107')
  print(requested_product)
import flask
from flask import render_template, redirect, render_template_string
from products_data import *
app = flask.Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/products')
def see_all_products():
  return render_template('products.html',products = all_products)

@app.route('/products/<product_id>')
def see_more_product(product_id):
  return render_template('see_more.html',product = retrieve_requested_product(product_id))
d
@app.route('/cart')
def see_cart():
  return render_template('cart.html', products=all_products, totals=[round(sum([p['Price'] for p in all_products]),2), len(all_products)])
# cart_item = [] 
@app.route('/add_prod/<product_id>')
def add_to_cart(product_id):
  add_cart(product_id)
  return 'bon'

@app.route('/delete_prod/<product_id>')
def del_to_cart(product_id):
  all_products.remove(retrieve_requested_product(product_id))
  return 'bad'

if __name__ == "__main__":
  app.run(debug=True)
import flask
from products_data import *
app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
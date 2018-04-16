# This contains the code for the flask server
from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Index"


@app.route('/draw')
def draw():
	return "draw"
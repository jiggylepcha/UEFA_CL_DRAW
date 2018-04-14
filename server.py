# This contains the code for the flask server
from flask import flask

app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World!'
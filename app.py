from flask import Flask
from flask_restful import Resource, Api
from random import randint, uniform
from flask import request
import json
import pickle
import sys

app = Flask(__name__)
api = Api(app)
stocks = {}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/stocks", methods = ['GET'])
def getStocks():
    b = {}
    try:
        with open('data.json', 'r') as f:
            b = json.load(f)
    except FileNotFoundError:
        b = {}
    return b

#
@app.route("/stocks", methods = ['POST'])
def postStocks():
    with open('data.json', 'w') as f:
        json.dump(request.json, f)
    return request.json


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

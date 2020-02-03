from flask import Flask
from flask_restful import Resource, Api
from random import randint, uniform
from flask import request
import json
import pickle
import sys
from sqlalchemy import create_engine
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///C:\\sqlitedbs\\school.db', echo=True)
Base = declarative_base()
eng = create_engine("sqlite://")
conn = eng.connect()
app = Flask(__name__)
api = Api(app)

@app.route('/')
def stock_streamer():
    return 'Welcome to the stock streamer server. See the stocks at localhost:5000/stocks'

@app.route("/stocks", methods = ['GET'])
def getStocks():
    stocks = {}
    try:
        with open('data.json', 'r') as f:
            stocks = json.load(f)
    except FileNotFoundError:
        print("file not found")
    return stocks

#
@app.route("/stocks", methods = ['POST'])
def postStocks():
    req = request.json
    with open('data.json', 'w') as f:
        json.dump(req, f)
    return req


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

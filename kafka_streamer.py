from flask import Flask
from flask_restful import Resource, Api
from flask import request
import json
import sys

import db_class

path='sqlite:///database/stocks_db.db'

app = Flask(__name__)
api = Api(app)

@app.route('/')
def stock_streamer():
    '''Root page welcome message'''
    return 'Welcome to the stock streamer server. See the stocks at localhost:5000/stocks'

@app.route("/stocks", methods = ['GET'])
def getStocks():
    '''Retrives the stock values from the database and renders it'''
    # Retrieve last database object
    db_obj = db_class.db(path)
    stocks = db_obj.getLastEntry()

    return stocks

@app.route("/stocks", methods = ['POST'])
def postStocks():
    '''Sends the stock values to the database'''
    # Get request
    req = request.json

    # Send to database
    db_obj = db_class.db(path)
    table_name = db_obj.getTable()
    db_obj.insertIntoDB(req, table_name)

    return req


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

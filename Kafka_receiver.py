import requests
import threading
import time
import datetime
import json
from collections import defaultdict

def run_get_request():
    '''
    Sends a get request to the kafka streamer and retrives the stock values every 30 seconds
    Prints the average values over time.
    '''
    # Reruns function every 0.1 seconds
    threading.Timer(30, run_get_request).start()
    # Get request to streamer to retrieve the stocks and parse into a dictionary with lists of the prices
    resp = requests.get("http://streamer:5000/stocks")
    arr = []
    for value in resp.json()["tickers"]:
      prices[value['name']].append(value["price"])
    # Print the timestamp with the retrieved and averaged
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    [print(key + ": " + str(round(sum(val)/len(val), 2)), flush=True) for key, val in prices.items()]
    print(timestamp, flush=True)

prices = defaultdict(list)

print("Starting the Kafka Receiver")
run_get_request()

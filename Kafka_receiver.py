import requests
import threading
import time
import datetime
import json
from collections import defaultdict


prices = defaultdict(list)

def run_get_request():
  threading.Timer(30, run_get_request).start()

  r = requests.get("http://streamer:5000/stocks")
  arr = []
  for v in r.json()["tickers"]:
      prices[v['name']].append(v["price"])

  timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
  [print(key + ": " + str(round(sum(val)/len(val), 2)), flush=True) for key, val in prices.items()]
  print(timestamp, flush=True)

print("starting kafka_receiver")
run_get_request()

import requests
from random import randint, uniform
import threading

def getTicker():
    names = [["AMZN",1902],["MSFT", 107],["AAPL", 215]]
    stocks = {names[i-1][0] : round(uniform(0.9, 1.1) * names[i-1][1]) for i in range(randint(1,4))}
    return stocks

def run_post_request():
  stock_dict = {"tickers":[{'name':key,"price":value} for key,value in getTicker().items()]}

  threading.Timer(0.1, run_post_request).start()

  r = requests.post("http://streamer:5000/stocks", json=stock_dict)
  print(r)

print("starting publisher")
run_post_request()

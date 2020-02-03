import requests
from random import randint, uniform
import threading

def getTicker():
    '''Creates random stocks +-10% base values given in worksheet

    Returns:
        stocks - dictionar containing the various stock values
    '''
    names = [["AMZN",1902],["MSFT", 107],["AAPL", 215]]
    stocks = {names[i-1][0] : round(uniform(0.9, 1.1) * names[i-1][1]) for i in range(randint(1,4))}
    return stocks

def run_post_request():
    '''Sends a post request to the kafka streamer with the stocks json every 0.1 seconds'''
    # Retrive the stock dictionary from getTickeer function
    stock_dict = {"tickers":[{'name':key,"price":value} for key,value in getTicker().items()]}
    # Reruns function every 0.1 seconds
    threading.Timer(0.1, run_post_request).start()
    # Sends a post request to the streamer
    request_resp = requests.post("http://streamer:5000/stocks", json=stock_dict)
    print("Posting data to stocks streamer: " + str(request_resp))

print("Starting Publisher")
run_post_request()

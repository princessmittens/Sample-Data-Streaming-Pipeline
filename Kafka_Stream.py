import requests
from random import randint, uniform
# data = None
# res = requests.get('http://localhost:5000/stocks')
# if res.ok:
#     data = res.json()
#     print(res.json())
def getTicker():
    names = [["AMZN",1902],["MSFT", 107],["AAPL", 215]]
    stocks = {names[i-1][0] : round(uniform(0.9, 1.1) * names[i-1][1]) for i in range(randint(1,4))}
    return stocks

stocks = getTicker()
stock_dict = {"tickers":[{'name':key,"price":value} for key,value in stocks.items()]}

r = requests.post("http://127.0.0.1:5000/stocks", json=stock_dict)
print(r)
# print(r.content)

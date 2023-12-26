'''
I stipulate a portfolio of 25% NVDA, 25% GOOGL, 25% AMZN, 25% MSFT.
'''
import requests
import yfinance as yf

with open("key.txt", "r") as file:
    API_KEY = file.read().strip()

START_DATE = "2016-03-20"
END_DATE = "2023-12-22"

data = {}

# Portfolio contains...
stocks = ["NVDA", "GOOGL", "AMZN", "MSFT"]

for stock in stocks:
    current_ticker = yf.Ticker(stock)
    print(current_ticker.history(period="1mo"))
    data[stock] = []

print(data)



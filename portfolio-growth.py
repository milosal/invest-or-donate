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

    dat = yf.download(current_ticker, start=START_DATE, end=START_DATE)
    start_price = dat["Open"][0] if not dat.empty else None

    dat = yf.download(current_ticker, start=END_DATE, end=END_DATE)
    end_price = dat["Open"][0] if not dat.empty else None

    data[stock] = [start_price, end_price]

print(data)



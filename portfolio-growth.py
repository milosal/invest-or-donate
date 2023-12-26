'''
I stipulate a portfolio of 25% NVDA, 25% GOOGL, 25% AMZN, 25% MSFT.
'''
import requests
import datetime 
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
print(API_KEY)
START_DATE = "2016-03-20"
END_DATE = "2023-12-22"

def convert_to_unix_time(date):
    return int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())

data = {}

# Portfolio contains...
stocks = ["NVDA", "GOOGL", "AMZN", "MSFT"]

# For each stock, get historical price 
for stock in stocks:

    params = {
    "symbol": "NVDA,GOOGL,AMZN,MSFT",
    "period1": START_DATE,
    "period2": END_DATE,
    "interval": "1d",
    "events": "history",
    }

    response = requests.get("https://query1.finance.yahoo.com/v7/finance/download", params=params)

    # Add to data dict if appropriate
    if response.status_code == 200:
        data[stock] = response.text
        print(data[stock])
    else:
        print(f"Failed. Status code: {response.status_code}")

#B7M49ARQFBP3BKBF
import requests
from matplotlib import pyplot
import pandas as pd
from pandas import DataFrame
def TIME_SERIES_INTRADAY():
    url_a = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
    stock = input("Enter Stock Name")
    url_b = '&interval=5min&outputsize=full&apikey=B7M49ARQFBP3BKBF'
    TIME_SERIES_INTRADAY_url = url_a+stock+url_b
    data = requests.get(TIME_SERIES_INTRADAY_url).json()
    open = []
    close = []
    high = []
    low = []
    volume = []
    time_stamp = []
    for i,j in data["Time Series (5min)"].items():
        time_stamp.append(i)
        open.append(j["1. open"])
        close.append(j["4. close"])
        high.append(j["2. high"])
        volume.append(j["5. volume"])
        low.append(j["3. low"])
    df = DataFrame(list(zip(time_stamp,open,close,high,low,volume)),columns=['time_stamp','open','close','high','low','volume'])
    print(df)
TIME_SERIES_INTRADAY()

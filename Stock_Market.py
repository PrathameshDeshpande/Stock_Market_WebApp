#B7M49ARQFBP3BKBF
import streamlit as st
import requests
from matplotlib import pyplot as plt
import pandas as pd
import datetime
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objects as go
st.title("STOCK MARKET")
st.write("## Made by Prathamesh with ❤️")
st.write("### Write The Name Of A Stock You Want To Study 👇👇")
stock=st.text_input("NAME OF THE STOCK :", "")
st.write("### Please Select Graph Style Below 👇👇")
graph_type=st.selectbox("Select Graph Type",("Line Graph","Candle Graph","Both (Line & Bar Graph)"))
st.write("### Please Select The Category Below 👇👇")
category =st.selectbox("Select Category Type",("TIME_SERIES_INTRADAY","TIME_SERIES_DAILY"))
b=st.button("SUBMIT")


@st.cache
def MAIN(stock,graph_type,category):
    if category == "TIME_SERIES_INTRADAY":
        TIME_SERIES_INTRADAY(stock,graph_type)
    elif category == "TIME_SERIES_DAILY":
        TIME_SERIES_DAILY(stock,graph_type)


def TIME_SERIES_INTRADAY(stock,graph_type):
    url_a = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
    url_b = '&interval=5min&apikey=B7M49ARQFBP3BKBF'
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
    df["time_stamp"] = df['time_stamp'].astype('datetime64[ns]')
    df2 = df.iloc[:85,:]
    if graph_type == "Candle Graph":
        fig = go.Figure(data=[go.Candlestick(x=df['time_stamp'],
                                         open=df2['open'],
                                         high=df2['high'],
                                         low=df2['low'],
                                         close=df2['close'])])
        fig.show()
    elif graph_type == "Line Graph":
        fig = px.line(df2, x='time_stamp', y='high')
        fig.show()
    elif graph_type == "Both (Line & Bar Graph)":
        fig = go.Figure(data=[go.Candlestick(x=df['time_stamp'],
                                         open=df2['open'],
                                         high=df2['high'],
                                         low=df2['low'],
                                         close=df2['close'])])
        fig.show()
        fig = px.line(df2, x='time_stamp', y='high')
        fig.show()


def TIME_SERIES_DAILY(stock,graph_type):
    url_a = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url_b = '&apikey=B7M49ARQFBP3BKBF'
    TIME_SERIES_INTRADAY_url = url_a + stock + url_b
    data = requests.get(TIME_SERIES_INTRADAY_url).json()
    open = []
    close = []
    high = []
    low = []
    volume = []
    time_stamp = []
    for i, j in data["Time Series (Daily)"].items():
        time_stamp.append(i)
        open.append(j["1. open"])
        close.append(j["4. close"])
        high.append(j["2. high"])
        volume.append(j["5. volume"])
        low.append(j["3. low"])
    df = DataFrame(list(zip(time_stamp, open, close, high, low, volume)),
                   columns=['time_stamp', 'open', 'close', 'high', 'low', 'volume'])
    df["time_stamp"] = df['time_stamp'].astype('datetime64[ns]')
    if graph_type == "Candle Graph":
        fig = go.Figure(data=[go.Candlestick(x=df['time_stamp'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'])])

        fig.show()
    elif graph_type == "Line Graph":
        fig = px.line(df, x='time_stamp', y='high')
        fig.show()
    elif graph_type == "Both (Line & Bar Graph)":
        fig = go.Figure(data=[go.Candlestick(x=df['time_stamp'],
                                         open=df2['open'],
                                         high=df2['high'],
                                         low=df2['low'],
                                         close=df2['close'])])
        fig.show()
        fig = px.line(df2, x='time_stamp', y='high')
        fig.show()
if b:
    MAIN(stock,graph_type,category)


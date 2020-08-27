#B7M49ARQFBP3BKBF
import streamlit as st
import requests
from matplotlib import pyplot as plt
import pandas as pd
import datetime
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objects as go
import random
st.markdown("<h1 style='text-align: center; color: black;'>📈💰STOCK MARKET ANALYSIS🤑📉</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Made by Prathamesh with ❤️ For Investors </h1>", unsafe_allow_html=True)
st.write("### Write The Name Of A Stock You Want To Study 👇👇")
stock=st.text_input("NAME OF THE STOCK :", "")
st.write("### Please Select Graph Style Below 👇👇")
graph_type=st.selectbox("Select Graph Type 📊",("Line Graph","Candle Graph","Both (Line & Bar Graph)"))
st.write("### Please Select The Category Below 👇👇")
category =st.selectbox("Select Category Type",("TIME_SERIES_INTRADAY","TIME_SERIES_DAILY","TIME_SERIES_MONTHLY"))
st.write("### Please Select The Box Below for Moving Point Average👇👇")
ch = st.checkbox("ANALYSIS MOVING POINT AVERAGE GRAPH")
if ch:
    interval = st.selectbox(
    'Please Select A Interval For Moving Point Avegrage',
    ('1min','5min','15min','30min','60min','daily','weekly','monthly'))
    time_period = st.slider(
    'Select a range of values for time period',
    60.0, 200.0)
    series_type = st.selectbox(
    'Please Select Desired Price Type in the Time Series',
    ('close','open','high','low'))
    v =True
else:
    interval = None
    time_period = None
    series_type = None
    v =False

b=st.button("SUBMIT")

def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )
_max_width_()
@st.cache(suppress_st_warning=True)
def MAIN(stock,graph_type,category,interval,time_period,series_type,v):
    _max_width_()
    if category == "TIME_SERIES_INTRADAY":
        st.write("### TIME SERIES INDRADAY GRAPH 👇👇")
        TIME_SERIES_INTRADAY(stock,graph_type)
    elif category == "TIME_SERIES_DAILY":
        st.write("### TIME SERIES DAILY GRAPH 👇👇")
        TIME_SERIES_DAILY(stock,graph_type)
    elif category == "TIME_SERIES_MONTHLY":
        st.write("### TIME SERIES MONTHLY GRAPH 👇👇")
        TIME_SERIES_MONTHLY(stock,graph_type)
    if v:
       interval = str(interval)
       time_period = str(int(time_period))
       series_type = str(series_type)
       st.write("### MOVING POINT AVERAGE GRAPH 👇👇")
       SMA(stock,interval,time_period,series_type)
    x = random.randrange(10)
    if x == 0:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Markets can stay irrational longer than you can stay solvent⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==2:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐When the tide goes out, you see who's swimming naked⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==3:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐If you don't understand it, then put your life savings into it⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==4:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Bulls make money, bears make money, pigs get slaughtered,Don't Be a Pig⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==5:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐It's a market of stocks, not a stock market⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==6:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐The trend is your friend⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==7:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐If you have trouble imagining a 20 percent loss in the stock market, you shouldn't be in stocks⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    elif x==8:
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐Investing should be more like watching paint dry or watching grass grow⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    else :
        st.write("### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐How many millionaires do you know who have become wealthy by investing in savings accounts?⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    
        



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
        fig = go.Figure(data=[go.Candlestick(x=df2['time_stamp'],
                                         open=df2['open'],
                                         high=df2['high'],
                                         low=df2['low'],
                                         close=df2['close'])])
        fig.update_layout(title='Candle Graph', autosize=False,
                  width=1400, height=800,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
    elif graph_type == "Line Graph":
        fig = px.line(df2, x='time_stamp', y='high',title="Line Graph")
        fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
    elif graph_type == "Both (Line & Bar Graph)":
        fig = go.Figure(data=[go.Candlestick(x=df2['time_stamp'],
                                         open=df2['open'],
                                         high=df2['high'],
                                         low=df2['low'],
                                         close=df2['close'])])
        fig.update_layout(title='Candle Graph', autosize=False,
                  width=1400, height=800,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
        fig = px.line(df2, x='time_stamp', y='high')
        fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)


def TIME_SERIES_DAILY(stock,graph_type):
    url_a = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url_b = '&apikey=B7M49ARQFBP3BKBF'
    TIME_SERIES_DAILY_url = url_a + stock + url_b
    data = requests.get(TIME_SERIES_DAILY_url).json()
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

        fig.update_layout(title='Candle Graph', autosize=False,
                  width=1400, height=800,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
    elif graph_type == "Line Graph":
        fig = px.line(df, x='time_stamp', y='high')
        fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
    elif graph_type == "Both (Line & Bar Graph)":
        fig = go.Figure(data=[go.Candlestick(x=df['time_stamp'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'])])
        fig.update_layout(title='Candle Graph', autosize=False,
                  width=1400, height=800,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
        fig = px.line(df, x='time_stamp', y='high')
        fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
def TIME_SERIES_MONTHLY(stock,graph_type):
    url_a = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='
    url_b = '&apikey=B7M49ARQFBP3BKBF'
    TIME_SERIES_MONTHLY_url = url_a + stock + url_b
    data = requests.get(TIME_SERIES_MONTHLY_url).json()
    open = []
    close = []
    high = []
    low = []
    volume = []
    time_stamp = []
    for i, j in data["Monthly Time Series"].items():
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

        fig.update_layout(title='Candle Graph', autosize=False,
                  width=1400, height=800,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
    elif graph_type == "Line Graph":
        fig = px.line(df, x='time_stamp', y='high')
        fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
    elif graph_type == "Both (Line & Bar Graph)":
        fig = go.Figure(data=[go.Candlestick(x=df['time_stamp'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'])])
        fig.update_layout(title='Candle Graph', autosize=False,
                  width=1400, height=800,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
        fig = px.line(df, x='time_stamp', y='high')
        fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
def SMA(stock,interval,time_period,series_type):
    url_a = 'https://www.alphavantage.co/query?function=SMA&symbol='
    url_b = '&apikey=B7M49ARQFBP3BKBF'
    SMA_url = url_a + stock + "&interval=" +interval+"&time_period="+time_period+"&series_type="+ series_type+ url_b
    print(SMA_url)
    data = requests.get(SMA_url).json()
    time_stamp = []
    sma = []
    for i,j in data["Technical Analysis: SMA"].items():
        time_stamp.append(i)
        sma.append(j["SMA"])
    df = DataFrame(list(zip(time_stamp,sma)),
                   columns=['time_stamp','sma'])
    df["time_stamp"] = df['time_stamp'].astype('datetime64[ns]')
    fig = px.line(df, x='time_stamp', y='sma')
    fig.update_layout(title='Line Graph', autosize=False,
                  width=1400, height=700,xaxis_title="TIME",
                  yaxis_title="PRICE",
                  legend_title="Legend Title",
                  font=dict(
                  family="Courier New, monospace",
                  size=18,
                  color="RebeccaPurple"),
                  margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)
    
if b:
    MAIN(stock,graph_type,category,interval,time_period,series_type,v)



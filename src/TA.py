import pandas as pd
import dataCollection as dc

def movingAverage():
    prices = dc.stockInfo.prices200d[["Open", "High", "Low", "Close"]]

    #Simple Moving Averages
    dc.stockInfo.taIndicators["SMA10"] = prices.rolling(10).mean().iloc[-1].round(2) #10 day simple moving average
    dc.stockInfo.taIndicators["SMA20"] = prices.rolling(20).mean().iloc[-1].round(2) #20 day simple moving average
    dc.stockInfo.taIndicators["SMA50"] = prices.rolling(50).mean().iloc[-1].round(2) #50 day simple moving average
    dc.stockInfo.taIndicators["SMA200"] = prices.rolling(200).mean().iloc[-1].round(2) #200 day simple moving average

    #Exponential Moving Average
    dc.stockInfo.taIndicators["EMA12"] = prices.ewm(12, adjust=False).mean().iloc[-1].round(2)
    dc.stockInfo.taIndicators["EMA26"] = prices.ewm(26, adjust=False).mean().iloc[-1].round(2)
    dc.stockInfo.taIndicators["EMA50"] = prices.ewm(50, adjust=False).mean().iloc[-1].round(2)
    dc.stockInfo.taIndicators["EMA200"] = prices.ewm(200, adjust=False).mean().iloc[-1].round(2)
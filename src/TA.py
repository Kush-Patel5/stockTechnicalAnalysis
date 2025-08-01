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

def MACD():
    dc.stockInfo.taIndicators["MACD"] = dc.stockInfo.taIndicators["EMA12"] - dc.stockInfo.taIndicators["EMA26"]
    dc.stockInfo.taIndicators["Signal Line"] = dc.stockInfo.taIndicators["MACD"].ewm(9, adjust=False).mean()

def RSI():
    prices = dc.stockInfo.prices200d[["Open", "High", "Low", "Close"]]
    rsiCalc = pd.DataFrame()
    for pricePoint in ["Open", "High", "Low", "Close"]:
        prices["change_"+pricePoint] = prices[pricePoint].diff().round(2)
        prices["gains_"+pricePoint] = prices["change_"+pricePoint].mask(prices["change_"+pricePoint] < 0, 0.0)
        prices["losses_"+pricePoint] = -prices["change_"+pricePoint].mask(prices["change_"+pricePoint] > 0, 0.0)

        rsiCalc["gainsAVG_"+pricePoint] = prices["gains_"+pricePoint].rolling(14).mean().round(2)
        rsiCalc["lossesAVG_"+pricePoint] = prices["losses_"+pricePoint].rolling(14).mean().round(2)
        rsiCalc["RS_"+pricePoint] = rsiCalc["gainsAVG_"+pricePoint]/rsiCalc["lossesAVG_"+pricePoint]
        rsiCalc["RSI_"+pricePoint] = 100 - (100/(1+rsiCalc["RS_"+pricePoint]))

    rsiCalc.iloc[-1][["RSI_Open", "RSI_High", "RSI_Low", "RSI_Close"]]
    dc.stockInfo.taIndicators["RSI"] = [rsiCalc.iloc[-1][rsi] for rsi in ["RSI_Open", "RSI_High", "RSI_Low", "RSI_Close"]]
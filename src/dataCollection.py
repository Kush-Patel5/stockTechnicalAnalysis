import pandas as pd
import yfinance as yf

class stockInfo:    
    #Basic info
    stockTicker = None
    prices200d = None

    #TA Indicators
    taIndicators = pd.DataFrame()

def priceCollection():
    prices = yf.Ticker(stockInfo.stockTicker).history(period="200d").drop(["Dividends", "Stock Splits"], axis=1)
    prices[["Open", "High", "Low", "Close"]] = prices[["Open", "High", "Low", "Close"]].round(2)
    stockInfo.prices200d = prices
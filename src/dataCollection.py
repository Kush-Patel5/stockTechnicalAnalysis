import pandas as pd
import yfinance as yf

def priceCollection(stock, numOfDays):
    prices = yf.Ticker(stock).history(period=str(numOfDays)+"d").drop(["Dividends", "Stock Splits"], axis=1)
    prices[["Open", "High", "Low", "Close"]] = prices[["Open", "High", "Low", "Close"]].round(2)
    return prices
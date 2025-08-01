import pandas as pd
import dataCollection as dc
import TA

while True:
    dc.stockInfo.stockTicker = input("Stock Ticker (enter 'exit' to quit): ")
    if (dc.stockInfo.stockTicker == "exit"):
        break
    dc.priceCollection()
    TA.movingAverage()
    TA.MACD()
    TA.RSI()

    print(dc.stockInfo.taIndicators.T)
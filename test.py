import yfinance as yf
import http.client


ticker = 'MSFT'
stock = yf.Ticker(ticker)

print(stock.fast_info)


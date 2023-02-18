import yfinance as yf
ticker = 'AAPL'
tic = yf.Ticker(ticker)
print(tic.fast_info)
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", period='5d',interval='2m')

#price = google.sustainability


data['Adj Close'].plot()
plt.show()
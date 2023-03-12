old_key = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']

new_key = ['Currency', 'Day High', 'Day Low', 'Stock Exchange', '50 day average', 'Last Price', 'Last Volume', 'Market cap', 'Opening price', 'Previous close', 'Quote type', 'Regular market previous close', 'Outstanding shares', '10 day average volume', '3-month average volume', 'Time zone', '200 day average', 'Year change', 'Year high', 'Year low']



key_mapping = dict(zip(old_key, new_key))
print(key_mapping)
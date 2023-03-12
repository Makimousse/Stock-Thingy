old_key = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']

new_key = ['', '', '', 'Quote type', ]

new_key_order = ['Currency','Time zone', 'Stock Exchange','Outstanding shares','Market cap','Opening price','Previous close','Regular market previous close','Day High','Day Low','Last Price','Last Volume','10 day average volume','3-month average volume','50 day average','200 day average','Year change','Year high','Year low','Quote type']

key_mapping = dict(zip(old_key, new_key))

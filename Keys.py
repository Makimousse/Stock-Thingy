list1 = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']

new_key = ['Currency', 'Day High', 'Day Low', 'Stock Exchange', '50 day average', 'Last Price', 'Last Volume', 'Market cap', 'Opening price', 'Previous close', 'Quote type', 'Regular market previous close', 'Outstanding shares', '10 day average volume', '3-month average volume', 'Time zone', '200 day average', 'Year change', 'Year high', 'Year low']



#Make dictionary to rearrange data


new_dict = {new_key:stock_info[old_info] for old_key, old_info in stock_info.items()}
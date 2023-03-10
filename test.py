import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt

# Create a Tkinter window
window = tk.Tk()
window.title("Stock Information")
window.geometry("800x1000")


# Function to get and update the historical graph with the current date_window input
def update_historical_graph():
    # Get the stock ticker and date window inputs from the user
    ticker = ticker_input.get()
    date_window = date_window_input.get()
    # Get the stock price data for the specified date window
    end_date = datetime.today() - timedelta(days=1)
    if 'y' in date_window:
        start_date = end_date - timedelta(days=365*int(date_window[:-1]))
    elif 'm' in date_window:
        start_date = end_date - timedelta(days=30*int(date_window[:-1]))
    elif 'd' in date_window:
        start_date = end_date - timedelta(days=int(date_window[:-1]))
    else:
        return
    data = yf.download(ticker, start=start_date, end=end_date)
    # Clear the previous graph
    ax.clear()
    # Plot the stock price data on the graph
    ax.plot(data.index, data['Adj Close'])
    ax.set_title(f"{ticker} Stock Price in USD")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (In USD)")
    fig.autofmt_xdate()
    canvas.draw()

# Create a title widget at the top of the window
title = tk.Label(window, text="Awesome Stock app", font=("Arial", 24))
title.pack(side="top", fill="x", pady=10)

# Create a label and input box for the ticker
ticker_label = tk.Label(window, text="Enter ticker:")
ticker_label.pack()
ticker_input = tk.Entry(window)
ticker_input.pack()

# Create a label and input box for the date window
date_window_label = tk.Label(window, text="Enter date window ('1y', '1m', or '1d'):")
date_window_label.pack()
date_window_input = tk.Entry(window)
date_window_input.pack()

# Create a button to display the historical graph
graph_button = tk.Button(window, text="Historical Graph", command=update_historical_graph)
graph_button.pack()

# Create a button to display the stock information
def display_stock_info():
    # Get the stock information for the ticker entered in the input box
    ticker = ticker_input.get()
    try:
        stock = yf.Ticker(ticker)
        old_info = stock.fast_info
        # Clear the text widget
        text.delete('1.0', 'end')
        # Define the new key names in the desired order
        old_key = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']
        new_key = ['Currency', 'Day High', 'Day Low', 'Stock Exchange', '50 day average', 'Last Price', 'Last Volume', 'Market cap', 'Opening price', 'Previous close', 'Quote type', 'Regular market previous close', 'Outstanding shares', '10 day average volume', '3-month average volume', 'Time zone', '200 day average', 'Year change', 'Year high', 'Year low']
        # Creating new dictionary with new_key as keys and corresponding values
        new_info = {}
        for new_key, old_key in zip(new_key, old_key):
            new_info[new_key] = old_info[old_key]
        new_key_order = ['Quote type','Currency','Time zone', 'Stock Exchange','Outstanding shares','Market cap','Opening price','Previous close','Regular market previous close','Day High','Day Low','Last Price','Last Volume','10 day average volume','3-month average volume','50 day average','200 day average','Year change','Year high','Year low']
        new_info = {new_key: new_info[new_key] for new_key in new_key_order}
        for key, value in new_info.items():
            text.insert('end', f"{key}: {value}\n\n")
    except:
        # Display an error message on the text widget
        text.delete('1.0', 'end')
        text.insert('end', "An error occurred while fetching stock information. Please try again with other values.\n")

# Create a button to display the stock information
info_button = tk.Button(window, text="Display Info", command=display_stock_info)
info_button.pack()

# Create a text widget to display the stock information
text = tk.Text(window)
text.pack()

# Create a Quit button to close the window
def quit_window():
    window.destroy()

quit_button = tk.Button(window, text="Quit", fg='red', command=quit_window)
quit_button.pack()

# Create a FigureCanvasTkAgg object for displaying the historical graph
fig, ax = plt.subplots(figsize=(8,6))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()


window.mainloop()

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt
import json

# Function to get and update the historical graph with the current date_window input
def update_historical_graph():
    ticker = ticker_input.get()
    date_window = date_window_input.get()

    # Fetches the determined date window from get_start_and_end_date
    start_date, end_date = get_start_and_end_date(date_window)
    if start_date is None or end_date is None:
        return
    # Downloads the stock price information from the date window
    data = yf.download(ticker, start=start_date, end=end_date)
    # Plot the stock price data on the graph
    ax.clear()
    ax.plot(data.index, data['Adj Close'])
    ax.set_title(f"{ticker} Stock Price in USD")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (In USD)")
    fig.autofmt_xdate()
    canvas.draw()

# Function to fetch the date window for the historical graph
def get_start_and_end_date(date_window):
    end_date = datetime.today() - timedelta(days=1)
    if 'y' in date_window:
        start_date = end_date - timedelta(days=365*int(date_window[:-1]))
    elif 'm' in date_window:
        start_date = end_date - timedelta(days=30*int(date_window[:-1]))
    elif 'd' in date_window:
        start_date = end_date - timedelta(days=int(date_window[:-1]))
    else:
        return None, None
    return start_date, end_date


def display_stock_info():
    ticker = ticker_input.get()
    # Uses a try and except function to manage errors
    try:
        # Gets the data for the ticker
        stock = yf.Ticker(ticker)
        old_info = stock.fast_info
        # Reads the reformulated keys from an external json file
        nk_open = open("new_keys.json", "r")
        new_keys = json.load(nk_open)
        # Creates a new dictionary that will host the corrected data information and order
        new_info = {}
        # Associates the values of fast_info with the reformulated keys of new_keys
        for key, val in old_info.items():
            if key in new_keys:
                new_key = new_keys[key]
            else:
                new_key=key
            new_info[new_key] = val
        # Reads the categorized keys from an external json file
        nko_open = open("new_key_order.json", "r")
        new_key_order = json.load(nko_open)
        # Applies the new order on the information dictionary
        new_info = {new_key: new_info[new_key] for new_key in new_key_order}
        # Clear the text widget and display the data
        text.delete('1.0', 'end')
        for key, value in new_info.items():
            text.insert('end', f"{key}: {value}\n\n")
    except:
        # Clears the text widget and displays an error message
        text.delete('1.0', 'end')
        text.insert('end', "An error occurred while fetching stock information. Please try again with other values.\n")


# Create a Tkinter window
window = tk.Tk()
window.title("Stock Information")
window.geometry("800x1000")

# Title for the window
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

# Create a button to display the historical graph with the update_historical_graph function
graph_button = tk.Button(window, text="Historical Graph", command=update_historical_graph)
graph_button.pack()

# Create a button to display the stock information with the display_stock_info function
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
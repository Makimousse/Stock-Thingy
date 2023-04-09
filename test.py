import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt
import json
import requests

def update_historical_graph():
    ticker = ticker_input.get()
    ticker2 = ticker_input2.get()
    date_window = date_window_input.get()
    start_date, end_date = get_start_and_end_date(date_window)
    if start_date is None or end_date is None:
        return
    data = yf.download(ticker, start=start_date, end=end_date)
    data2 = yf.download(ticker2, start=start_date, end=end_date)
    ax.clear()
    ax.plot(data.index, data['Adj Close'], label=ticker)
    ax.plot(data2.index, data2['Adj Close'], label=ticker2)
    ax.set_title("Stock Price in USD")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (In USD)")
    ax.legend()
    fig.autofmt_xdate()
    canvas.draw()

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
    try:
        stock = yf.Ticker(ticker)
        old_info = stock.fast_info
        response = requests.get("https://raw.githubusercontent.com/Makimousse/Stock-Thingy/main/new_keys.json")
        new_keys = json.loads(response.content)
        new_info = {}
        for key, val in old_info.items():
            if key in new_keys:
                new_key = new_keys[key]
            else:
                new_key=key
            new_info[new_key] = val
        response = requests.get("https://raw.githubusercontent.com/Makimousse/Stock-Thingy/main/new_key_order.json")
        new_key_order = json.loads(response.content)
        new_info = {new_key: new_info[new_key] for new_key in new_key_order}
        text.delete('1.0', 'end')
        for key, value in new_info.items():
            text.insert('end', f"{key}: {value}\n\n")
    except:
        text.delete('1.0', 'end')
        text.insert('end', "An error occurred while fetching stock information. Please try again with other values.\n")

window = tk.Tk()
window.title("Stock Information")
window.geometry("800x1000")
title = tk.Label(window, text="Awesome Stock app", font=("Arial", 24))
title.pack(side="top", fill="x", pady=10)

ticker_label = tk.Label(window, text="Enter ticker:")
ticker_label.pack()
ticker_input = tk.Entry(window)
ticker_input.pack()

ticker_label2 = tk.Label(window, text="Enter another ticker (for graph):")
ticker_label2.pack()
ticker_input2 = tk.Entry(window)
ticker_input2.pack()

date_window_label = tk.Label(window, text="Enter date window ('1y', '1m', or '1d'):")
date_window_label.pack()
date_window_input = tk.Entry(window)
date_window_input.pack()

graph_button = tk.Button(window, text="Historical Graph", command=update_historical_graph)
graph_button.pack()
info_button = tk.Button(window, text="Display Info (for first ticker only)", command=display_stock_info)
info_button.pack()
text = tk.Text(window)
text.pack()
def quit_window():
    window.destroy()
quit_button = tk.Button(window, text="Quit", fg='red', command=quit_window)
quit_button.pack()
fig, ax = plt.subplots(figsize=(8,6))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
window.mainloop()
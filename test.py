import yfinance as yf
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def display_stock_info():
    # Get the stock information for the ticker entered in the input box
    ticker = ticker_input.get()
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    # Clear the text widget
    text.delete('1.0', 'end')
    # Insert the stock information into the text widget with first letter of each key capitalized
    for key, value in stock_info.items():
        capitalized_key = key.capitalize()
        text.insert('end', f"{capitalized_key}: {value}\n\n")
        
        # Hide the graph
        graph_frame.grid_forget()
        
def display_historical_graph():
    # Get the stock ticker and date range entered by the user
    ticker = ticker_input.get()
    date_window = date_window_input.get()

    # Define the start and end dates of the date range
    if date_window == "1y":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
    elif date_window == "1m":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    elif date_window == "1d":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)
    else:
        # Invalid date range
        return

    # Get the historical data for the specified date range
    data = yf.download(ticker, start=start_date, end=end_date)

    # Plot the historical data on a graph
    fig = Figure(figsize=(6, 5), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(data["Close"])
    plot.set_title(f"{ticker} Historical Data ({start_date.date()} - {end_date.date()})")
    plot.set_xlabel("Date")
    plot.set_ylabel("Price")

    # Display the graph in a Tkinter window
    graph_frame = ttk.Frame(window, height=400, width=500)
    graph_frame.grid(row=1, column=1, columnspan=2)
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Place the graph over the text widget
    text.grid_forget()
    graph_frame.lift()

# Create a Tkinter window
window = tk.Tk()
window.title("Stock Information")

window.geometry("800x600")

# Create a label and input box for the ticker
ticker_label = tk.Label(window, text="Enter ticker:")
ticker_label.pack(side=tk.LEFT, padx=10, pady=10)
ticker_input = tk.Entry(window)
ticker_input.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label and input box for the date window
date_window_label = tk.Label(window, text="Enter date window (e.g. 1y, 1m, 1d):")
date_window_label.pack(side=tk.LEFT, padx=10, pady=10)
date_window_input = tk.Entry(window)
date_window_input.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button to display the stock information
info_button = tk.Button(window, text="Display Info", command=display_stock_info)
info_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button to display the stock graph
graph_button = tk.Button(window, text="Historical Graph", command=display_historical_graph)
graph_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a text widget to display the stock information
text = tk.Text(window, width=50, height=30)
text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a canvas to display the stock graph
fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack_forget()

# Create a Quit button to close the window
def quit_window():
    window.destroy()

quit_button = tk.Button(window, text="Quit", bg='#fc0303', command=quit_window)
quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

window.mainloop()

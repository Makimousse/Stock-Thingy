import tkinter as tk
import yfinance as yf

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


# Create a Tkinter window
window = tk.Tk()
window.title("Stock Information")

# Create a label and input box for the ticker
ticker_label = tk.Label(window, text="Enter ticker:")
ticker_label.pack()
ticker_input = tk.Entry(window)
ticker_input.pack()

# Create a button to display the stock information
info_button = tk.Button(window, text="Display Info", command=display_stock_info)
info_button.pack()

# Create a text widget to display the stock information
text = tk.Text(window)
text.pack()

# Create a Quit button to close the window
def quit_window():
    window.destroy()

quit_button = tk.Button(window, text="Quit", command=quit_window, fg='red')
quit_button.pack()

window.mainloop()
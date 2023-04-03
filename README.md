# Stock Information Application
This is a Python application to fetch and display stock information and historical prices for a given ticker. It uses the tkinter module for creating a GUI window, yfinance module for fetching stock information, and matplotlib module for displaying the historical prices.

## Getting Started
Prerequisites:
- Python 3.x
- tkinter, yfinance, and matplotlib modules.
## Installation
The required modules can be installed via pip:

pip install tkinter yfinance matplotlib
## Usage
After installing the required modules, run the script stock_info_gui.py and enter the ticker and date window. The application has two buttons, one to display the historical graph, and the other to display the stock information.

## Running the application
To run the application, execute the stock_info_gui.py file in the terminal or run it via an IDE.

## Application Structure
The stock_info_gui.py file is the main entry point to the application. The application has the following functions:
- update_historical_graph(): This function updates the historical graph based on the entered ticker and date window. It uses the yfinance module to fetch the stock price information for the entered date range, and matplotlib to plot the stock price data on the graph.
- get_start_and_end_date(date_window): This function returns the start and end dates for the entered date window. It takes the date window as input, calculates the start and end dates based on the date window, and returns them.
- display_stock_info(): This function displays the stock information for the entered ticker. It uses the yfinance module to fetch the stock information, reformats the information to a user-friendly format, and displays it on a text widget.
## GUI components
The GUI components are created using the tkinter module. The following components are used in the application:
- tk.Label: This is used to create labels for the ticker, date window, and title.
- tk.Entry: This is used to create input boxes for the ticker and date window.
- tk.Button: This is used to create buttons for displaying the historical graph and stock information, and for quitting the application.
- tk.Text: This is used to display the stock information.

## Code sources:
Some of the code in this project was inspired by/sourced from online resources. You may find these sources below:
- Stack Overflow (https://stackoverflow.com/)
- Graphical User Interfaces with Tk (https://docs.python.org/3/library/tk.html)
- Tkinter tutorial (https://www.pythonguis.com/tkinter-tutorial/)
- Python GUI Programming With Tkinter (https://realpython.com/python-gui-tkinter/)
- PyPI - yfinance (https://pypi.org/project/yfinance/)
- yfinance Library – A Complete Guide (https://algotrading101.com/learn/yfinance-guide/)
- datetime — Basic date and time types (https://docs.python.org/3/library/datetime.html)
- Matplotlib tutorials (https://matplotlib.org/stable/tutorials/index)
- PyPI - Matplotlib (https://pypi.org/project/matplotlib/)
- Python | Introduction to Matplotlib (https://www.geeksforgeeks.org/python-introduction-matplotlib/)

As a supplementary resource, ChatGPT was utilized as a final measure to address coding challenges, effectively resolving file and source-code editor-related concerns, among others.
## License
This project is licensed under the MIT License.




# Stock Information App
This app is designed to display stock information and a historical graph for a given stock ticker.

## Requirements:
This code requires the following Python packages:
- tkinter
- matplotlib
- yfinance

## Usage:
To use this app, simply run the code in a Python environment. A window will appear with the following features:

- A title widget at the top of the window displaying "Awesome Stock app"
- A label and input box for the ticker
- A label and input box for the date window
- A button to display the historical graph
- A button to display the stock information
- A text widget to display the stock information
- A Quit button to close the window

## Historical Graph:
To display the historical graph, enter a stock ticker and a date window ('1y', '1m', or '1d') and click the "Historical Graph" button. The graph will display the adjusted close stock price for the specified date window.

## Stock Information:
To display the stock information, enter a stock ticker and click the "Display Info" button.

## Notes:
This app uses the yfinance library to retrieve stock data and the matplotlib library to display the historical graph. The app is designed to handle user inputs that conform to the date window format specified above. Any other input will not produce a graph.

### License:
This code is published under the MIT license

# Using Screener
import pandas as pd
from pathlib import Path

from finviz.screener import Screener

filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
stock_list = Screener(filters=filters, table='Performance', order='price')  # Get the performance table and sort it by price ascending

# Export the screener results to .csv
stock_list.to_csv("stock.csv")

# Create a SQLite database
#stock_list.to_sqlite("stock.sqlite3")

for stock in stock_list[9:19]:  # Loop through 10th - 20th stocks
    print(stock['Ticker'], stock['Price']) # Print symbol and price

# Add more filters
#stock_list.add(filters=['fa_div_high'])  # Show stocks with high dividend yield
# or just stock_list(filters=['fa_div_high'])

# Print the table into the console
print()
print("Screener")
print("---------")
print()
print(stock_list)
print()





# Portfolio

from finviz.portfolio import Portfolio
portfolio = Portfolio('david_0187_finance@mail.com', 'Windfall#9', 'Watchlist 1: Trending Stocks')
# Print the portfolio into the console
print()
print("Portfolio")
print("---------")
print()
print(portfolio)
print()






#Individual stocks
import finviz
print()
print("Individual Stocks")
print("---------")
print()
#finviz.get_stock('AAPL')
print()


# Downloading charts
# Monthly, Candles, Large, No Technical Analysis
#stock_list.get_charts(period='m', chart_type='c', size='l', ta='0')

# period='d' > daily
# period='w' > weekly
# period='m' > monthly

# chart_type='c' > candle
# chart_type='l' > lines

# size='m' > small
# size='l' > large

# ta='1' > display technical analysis
# ta='0' > ignore technical analysis



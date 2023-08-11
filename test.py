import pandas as pd
import yfinance as yf
from pprint import pprint 
import requests
from bs4 import BeautifulSoup

dic = {
    'mike': ['mike', 20],
    'john': ['john', 32],
    'steve': ['steve', 19],
}
for key, val in dic.items():
    globals()[key] = [(val[0], val[1])]
print(mike)



    #print(x)
    #print(y)
   #globals()[x] = y

#print(mike)

'''
name = ['mike', 'john', 'steve']   
age = [20, 32, 19] 

for x,y in zip(name, age):
    globals()[x] = y

print(mike)
'''
'''
# get historical market data
hist = msft.history(period="1mo")


# show actions (dividends, splits, capital gains)
print("actions: ")
print(msft.actions)
print()

print("dividends: ")
print(msft.dividends)
print()

print("splits: ")
print(msft.splits)
print()


# show financials:
# - income statement
print("financials: ")
print(msft.financials)
print()


# - balance sheet
print("balance_sheet: ")
print(msft.balance_sheet)
print()


# - cash flow statement
print("cashflow: ")
print(msft.cashflow)
print()


# show holders
print("major_holders: ")
print(msft.major_holders, msft.institutional_holders, msft.mutualfund_holders)
print()
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
print("earnings: ")
print(msft.earnings)
print()

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print("isin: ")
print(msft.isin)
print()


# show options expirations
msft.options

# show news
msft.news

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts

'''





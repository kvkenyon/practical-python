# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name': row[0], 'share': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices

fn_portfolio = 'Data/portfolio.csv'
fn_prices = 'Data/prices.csv'

portfolio = read_portfolio(fn_portfolio)

total = 0.0
for s in portfolio:
    total += s['share'] * s['price'] 
print(total)

prices = read_prices(fn_prices)
#pprint(prices)

new_total = 0.0
for holding in portfolio:
    symbol = holding['name']
    buy_price = holding['price']
    curr_price = prices[symbol]
    print(symbol, 'Buy price:', buy_price)
    print(symbol, 'Current price:', curr_price)
    print('Profit/Loss:', curr_price - buy_price)
    print()
    new_total += holding['share'] * float(curr_price)

print('New total:', new_total)
print('Gain/Loss:', new_total-total)
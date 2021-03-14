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

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        symbol = holding['name']
        shares = holding['share']
        buy_price = holding['price']
        current_price = prices[symbol]
        change = current_price - buy_price 
        report.append((symbol, shares, current_price, change))
    return report

fn_portfolio = 'Data/portfolio.csv'
fn_prices = 'Data/prices.csv'

portfolio = read_portfolio(fn_portfolio)
prices = read_prices(fn_prices)
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
sep = ['-'*10] * len(headers)
print('%10s %10s %10s %10s' % tuple(sep))
for n, s, price, delta in report:
    price = '$' + str(round(price,2))
    print(f'{n: >10s} {s: >10d} {price: >10s} {delta: 10.2f}')

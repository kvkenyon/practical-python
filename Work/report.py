# report.py
#
# Exercise 2.4
import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        funcs = [str, int, float]
        indices = [headers.index(colname) for colname in select]
        return [{colname: func(row[index]) for func, colname, index in zip(funcs, select, indices)} for row in rows]

def read_prices(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        return {row[0]: float(row[1]) for row in rows if row}

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        symbol = holding['name']
        shares = holding['shares']
        buy_price = holding['price']
        current_price = prices[symbol]
        change = current_price - buy_price 
        report.append((symbol, shares, current_price, change))
    return report

fn_portfolio = 'Data/portfoliodate.csv'
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


total_cost = sum([s['price']*s['shares'] for s in portfolio])
print('Total cost:', total_cost)
# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name': row[0], 'share': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio(filename)
total = 0.0
for s in portfolio:
    total += s['share'] * s['price'] 
print(total)
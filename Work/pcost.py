# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        total_price = 0.0
        for lineno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_price = total_price + (shares * price)
            except ValueError:
                print(f"Row {lineno}: Couldn't convert:", row)
        return total_price
    raise RuntimeError

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
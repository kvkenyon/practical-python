# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)

        total_price = 0.0
        for row in rows:
            print(row)
            try:
                shares = int(row[1])
                price = float(row[2])
                total_price = total_price + (shares * price)
            except ValueError:
                print('Invalid input:', row)
        return total_price
    raise RuntimeError

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
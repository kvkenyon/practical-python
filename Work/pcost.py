# pcost.py
#
# Exercise 1.27

import os

print(os.getcwd())
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    total_price = 0.0
    for line in f:
        row = line.split(',')
        if row and len(row) == 3:
            shares = int(row[1])
            price = float(row[2])
            total_price = total_price + (shares * price)
    print(f'Total cost: {total_price}')        
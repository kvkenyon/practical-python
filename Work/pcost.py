#! /usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total_price = 0.0
    for record in portfolio: 
        shares = record['shares']
        price = record['price']
        total_price = total_price + (shares * price)
    return total_price

def main(argv):
    if len(argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
#! /usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv


def read_portfolio(filename):
    with open(filename) as file:
        return parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True) 


def read_prices(filename):
    with open(filename) as file:
        return dict(parse_csv(file, types=[str, float], has_headers=False))


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


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    sep = ['-'*10] * len(headers)
    print('%10s %10s %10s %10s' % tuple(sep))
    for n, s, price, delta in report:
        price = '$' + str(round(price,2))
        print(f'{n: >10s} {s: >10d} {price: >10s} {delta: 10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    """
    Creates the portfolio report
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    fn_portfolio = argv[1] 
    fn_prices = argv[2] 

    portfolio_report(fn_portfolio, fn_prices)

if __name__ == '__main__':
    import sys
    main(sys.argv)
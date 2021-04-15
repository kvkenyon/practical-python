#! /usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat


def read_portfolio(filename, **opts):
    with open(filename) as file:
        portdicts = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True, **opts) 
    portfolio = [Stock(**d) for d in portdicts]
    return Portfolio(portfolio)

def read_prices(filename):
    with open(filename) as file:
        return dict(parse_csv(file, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        symbol = holding.name 
        shares = holding.shares 
        buy_price = holding.price 
        current_price = prices[symbol]
        change = current_price - buy_price 
        report.append((symbol, shares, current_price, change))
    return report

def print_report(report, formatter):
    headers = ('Name', 'Shares', 'Price', 'Change')
    formatter.headings(headers)
    for n, s, price, delta in report:
        price = '$' + str(round(price,2))
        delta = str(round(delta, 2))
        rowdata = [n,s,price,delta]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    """
    Creates the portfolio report
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
      
def main(argv):
    fn_portfolio = argv[1] 
    fn_prices = argv[2] 
    fmt = 'txt'
    if len(argv) > 3:
        fmt = argv[3]


    portfolio_report(fn_portfolio, fn_prices, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)
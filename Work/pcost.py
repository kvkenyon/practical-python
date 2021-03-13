# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        next(f)
        total_price = 0.0
        for line in f:
            row = line.split(',')
            try:
                shares = int(row[1])
                price = float(row[2])
                total_price = total_price + (shares * price)
            except ValueError:
                print('Invalid input:', line)
        return total_price
    raise RuntimeError

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
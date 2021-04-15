# ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    import report 
    import tableformat

    formatter = tableformat.create_formatter(fmt)

    portfolio = report.read_portfolio(portfile)

    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio) 

    headers = ('Name', 'Price', 'Change')
    formatter.headings(headers)
    for row in rows:
        rowdata = [row['name'], row['price'], row['change']]
        formatter.row(rowdata)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        raise SystemError('Usage: ticker <porftile> <logfile> <fmt>')
    portfile = sys.argv[1]
    logfile = sys.argv[2]
    fmt = sys.argv[3]
    ticker(portfile, logfile, fmt)
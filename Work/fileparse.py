# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)

        if has_headers and select:
            indices = [headers.index(colname) for colname in select] 
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            if indices:
                row = [row[index] for index in indices]

            if types: 
                row = [conv(value) for value, conv in zip(row, types)]

            record = dict(zip(headers, row)) if has_headers else tuple(row)

            records.append(record)

    return records


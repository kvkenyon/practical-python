# fileparse.py
#
# Exercise 3.3

import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('Select requires headers.')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)

    if has_headers and select:
        indices = [headers.index(colname) for colname in select] 
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, start=1):
        try:
            if not row:    # Skip rows with no data
                continue

            if indices:
                row = [row[index] for index in indices]

            if types: 
                row = [conv(value) for value, conv in zip(row, types)]

            record = dict(zip(headers, row)) if has_headers else tuple(row)

            records.append(record)
        except ValueError as e:
            if silence_errors:
                continue
            log.warning(f"Row {rowno}: Couldn't convert {row}")
            log.debug(f'Row {rowno}: Reason {e}')

    return records


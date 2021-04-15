# tableformat.py

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h: >10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{str(d): >10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join([str(h) for h in headers])) 

    def row(self, rowdata):
        print(','.join([str(h) for h in rowdata])) 

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        r = '<tr>'
        for h in headers:
            r += f'<th>{h}</th>'
        r += '</tr>'
        print(r)

    def row(self, rowdata):
        r = '<tr>'
        for data in rowdata:
            r += f'<td>{data}</td>'
        r += '</tr>'
        print(r)

class FormatError(Exception):
    pass    

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    else:
        raise FormatError('Unknown table format: %s' % fmt)

def print_table(objects, attrs, fmt='txt'):
    formatter = create_formatter(fmt)

    formatter.headings(attrs)
    for obj in objects:
        rowdata = []
        for attr in attrs:
            val = getattr(obj, attr)
            rowdata.append(str(val))
        formatter.row(rowdata)
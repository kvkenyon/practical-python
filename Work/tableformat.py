# tableformat.py

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print('%10s %10s %10s %10s' % headers)
        sep = ['-'*10] * len(headers)
        print('%10s %10s %10s %10s' % tuple(sep))

    def row(self, rowdata):
        print(f'{rowdata[0]: >10s} {rowdata[1]: >10d} {rowdata[2]: >10s} {rowdata[3]: >10s}')

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
    

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        return CSVTableFormatter()
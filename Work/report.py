import os
import csv
import pprint

def read_portfolio(filename):
    
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):

    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

portfolio = read_portfolio("/Users/alex/practical-python/Work/Data/portfolio.csv")
prices = read_prices("/Users/alex/practical-python/Work/Data/prices.csv")


def make_report(portfolio, prices):

    rows = []

    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
thing = ('----------', '----------', '----------', '----------')

print('%10s %10s %10s %10s' % headers)
print('%10s %10s %10s %10s' % thing)

for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
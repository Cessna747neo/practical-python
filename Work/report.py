import os
import csv
os.chdir('/Users/alex/practical-python/Work/Data/')

def read_portfolio():
    
    portfolio = []

    with open('portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
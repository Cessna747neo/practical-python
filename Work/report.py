import csv

filename = "C:\Program Files\Git\practical-python\Work\Data\portfolio.csv"

def read_portfolio(filename):
    
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(stock)
    return portfolio

list = read_portfolio(filename)
print(list)
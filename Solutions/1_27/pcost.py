# pcost.py

total_cost = 0.0

with open("/Users/alex/practical-python/Work/Data/missing.csv", 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price

print('Total cost', total_cost)

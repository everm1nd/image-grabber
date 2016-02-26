import csv
from collections import defaultdict

d = defaultdict(set)
with open('sha.log.csv', 'rb') as csvfile:
    shadata = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE)
    for row in shadata:
        d[row[0]].add(row[2])

print d

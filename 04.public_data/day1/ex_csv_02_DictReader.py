import csv

f=open('dictdata1.csv')
reader=csv.DictReader(f)

for row in reader:
    print(row)

f.close()
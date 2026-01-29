# csv.DictWriter() 에제

import csv

fieldnames = ['id', 'name', 'price', 'amount']
data =[
    {'id':'1', 'name':'apple', 'price':'5000', 'amount':'5'},
    {'id':'2', 'name':'pencil', 'price':'500', 'amount':'42'},
    {'id':'3', 'name':'pineapple', 'price':'8000', 'amount':'5'},
    {'id':'4', 'name':'pen', 'price':'1500', 'amount':'10'}
]

f=open('dictdata1.csv', 'w')
writer=csv.DictWriter(f,fieldnames=fieldnames)

# DictWrite에 지정된 fieldnames로 헤더 저장
writer.writeheader()
for row in data:
    writer.writerow(row)

f.close()
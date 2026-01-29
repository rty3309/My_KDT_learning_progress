# 데이터 분석 : 누락 데이터 확인

import csv

f = open('daegu.csv', 'r', encoding='utf-8-sig')
data = csv.reader(f, delimiter=',')
for row in data:
    if '' in row:
        print(row)

f.close()
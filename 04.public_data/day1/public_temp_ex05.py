# 데이터 헤더 출력하기

import csv
f = open('daegu-utf8.csv', encoding='utf-8-sig')

data = csv.reader(f, delimiter=',')
header=next(data)    # next() : 한 행을 읽고 다음 행으로 이동
print(header)
f.close()
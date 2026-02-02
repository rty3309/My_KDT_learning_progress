# 대중교통 데이터 읽어오기

import csv

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)

header=next(data)    # 한 줄을 읽고 다음 줄로 이동
print(header)

i=1
for row in data:
    if i > 5:
        break
    print(row)
    i += 1
f.close()    # 숫자가 문자열로 되어 있는 것 확인
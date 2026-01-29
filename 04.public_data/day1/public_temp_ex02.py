# 대구 기온 데이터 확인

import csv

f = open('daegu.csv', 'r', encoding='utf-8')

reader = csv.reader(f, delimiter=',')
count = 0

for row in reader:    # reader 객체를 이용하여 csv 파일에서 한 라인씩 읽음
    if count > 5:
        break
    else:
        print(row)
    count += 1

f.close()
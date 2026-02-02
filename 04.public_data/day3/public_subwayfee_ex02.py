# 전체 탑승 인원 대비 유임 승차 비율이 가장 높은 역은?

import csv

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
max_rate=0

for row in data:
    row[4] = int(row[4])    # 4,6 컬럼 값을 정수로 변환
    row[6] = int(row[6])

    rate = row[4]/row[6]    # [6]컬럼의 값이 0인 행 확인 용도
    if rate > max_rate:
        max_rate = rate

print(max_rate)
f.close()
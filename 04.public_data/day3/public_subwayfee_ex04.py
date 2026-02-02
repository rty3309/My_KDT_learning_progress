# 최대 무임 승차 비율 확인

import csv

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
max_rate=0
max_row=[]
fee=4; free=6    # 유임승차 및 무임승차 인덱스
# fee, free = 4, 6 원래는 이렇게 썼었음

for row in data:
    row[fee]=int(row[fee])
    row[free]=int(row[free])

    if row[free] !=0:    # 무임승차인원이 0이 아닌 역만 계산
        rate=(row[free]*100)/(row[fee]+row[free])
        if rate > max_rate:
            max_rate=rate
            max_row=row
            print(f'{max_row}: {round(max_rate, 2)}%')

print('무임 승차 비율이 최대인 역 정보')
print(f'{max_row}: {max_rate}%')
f.close()
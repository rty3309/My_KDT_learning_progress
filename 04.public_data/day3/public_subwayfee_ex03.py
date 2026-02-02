# 무임승차 인원이 0인 역 찾기

import csv

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)

fee=4    # 유임승차 인덱스
free=6    # 무임승차 인덱스

for row in data:
    row[fee]=int(row[fee])
    row[free]=int(row[free])
    # rate = 유임승차인원/전체탑승인원(유임승차+무임승차)
    rate=row[fee]/(row[fee]+row[free])

    if row[free]==0:    # 무임승차 인원[6]이 없는 역 출력
        print(row)

f.close()
# ['Dec.25', '경의선', '1295', '김포공항', 3, '0 ', 0, '0 ']
                                                 # ㄴ 이 0은 무임승차 인원수
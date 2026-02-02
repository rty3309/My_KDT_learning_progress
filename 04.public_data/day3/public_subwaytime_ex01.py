# 시간대별 지하철 이용 인원 수

import csv

result=[]
total_number=0

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)    # 2줄의 헤더 정보를 건너뜀
    next(data)

    for row in data:
        row[4:]=map(int,row[4:])    # 문자열을 숫자로 변경 후 원래의 위치에 저장
        total_number += row[4]    # [4] 04:00 ~ 04:59의 승차 인원으 모두 더함
        result.append(row[4])

print(f'총 지하철 역의 수: {len(result)}')
print(f'새벽 4시 승차인원: {total_number:,}')
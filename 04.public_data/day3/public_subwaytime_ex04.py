# 출근 시간대 승차 인원이 많은 10개의 역 이름 찾기

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)    # 2줄의 헤더 정보 건너뜀
    next(data)
    result=[]

    station_list = []

    for row in data:
        row[4:] = map(int, row[4:])
        passenger_num = sum(row[10:15:2])    # index 10, 12, 14
        station_name = row[3] + '('+ row[1] +')'
        # 튜플(역이름, 승차인원) 형태로 리스트에 저장
        station_list.append((station_name, passenger_num))

sorted_passenger_list=sorted(station_list,
                             key=lambda x: x[1],
                             reverse=True)

# 승차인원 기준 내림차순 정렬된 10개 역의 이름 및 승차 인원 출력
index=1
for station in sorted_passenger_list[:10]:    # 0, 1, ..., 9 총 10개
    print(f'[{index}]: {station[0]} {station[1]:,}')
    index +=1

station_name, station_passenger = zip(*sorted_passenger_list[:10])

# zip(*리스트): 아래 for 구문과 동일 기능
# for name, num in sorted_passenger_list[:10]:
#   station_name.append(name)
#   station_passenger.append(num)

plt.figure(figsize=(8,6))

plt.title('출근 시간대 승차 인원이 가장 많은 10개 역', size=16)
plt.bar(range(len(station_passenger)), station_passenger)

plt.xticks(range(len(station_name)), station_name,
           rotation=70, fontsize=8)
plt.ylabel('승차인원수')
plt.tight_layout()    # 최소한의 여백 생성
plt.show()
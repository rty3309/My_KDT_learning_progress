# 공공데이터 과제 #3
# KDT 12기 이재헌

# 1. 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원을 출력하시오.

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    data = list(data)
    station_list = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']
    max_station_list = []
    max_num_list = []

    for i in range(7):
        max_num = -1
        max_station = ''
        for row in data:
            if row[1] == station_list[i]:
                row[4:] = map(int, row[4:])
                row_sum = sum(row[11:14:2])    # index 11, 13(7시 하차, 8시 하차)
                if row_sum > max_num:
                    max_num = row_sum
                    max_station = row[3]
        max_station_list.append(max_station)
        max_num_list.append(max_num)
        print(f'출근 시간대 {i+1}호선 최대 하차역 :',
            f'{max_station}역, 하차인원: {max_num:,}명')

x_labels = [f"{line} {station}" for line, station in zip(station_list, max_station_list)]
# 컴프리헨션으로 이름으로 쓸 두 리스트를 zip 해서 line, station 변수로 불러와서 원하는 형태로 리스트 생성

plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.bar(range(len(max_num_list)), max_num_list)
plt.xticks(range(len(max_station_list)), x_labels, rotation=80, fontsize=8)
plt.tight_layout()
plt.show()

# 총 승차 인원 대비 유임 승차 비율이 50% 이하인 역

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data); print(header)
min_rate=100
min_row=[]
min_total_count=0
fee=4; free=6    # 유임승차 및 무임승차 인덱스

for row in data:
    row[fee]=int(row[fee])
    row[free]=int(row[free])
    total_count = row[fee]+row[free]
    # 무임승차 인원이 없고, 총 승차인원이 1만명 이상
    if (row[free] != 0) and (total_count >=10000):
        rate=row[fee]/total_count
        if rate <=0.5:    # 유임승차 비율이 50%이하
            print(row, round(rate*100,1))
            # 유임승차 비율이 가장 낮은 역 찾기
            if rate < min_rate:
                min_rate = rate
                min_row = row
                min_total_count=total_count
f.close()

print()
print(f'유임 승차 비율이 가장 낮은 역: {min_row[1]} {min_row[3]} ')
print(f'전체 인원: {min_total_count:,}명, ',
      f'유임승차인원: {min_row[fee]:,}명, ',
      f'유임승차비율: {round(min_rate*100 , 1)}%')

plt.title(min_row[3]+'역 유,무임 승차 비율')
label=['유임승차','무임승차']
values=[min_row[fee], min_row[free]]
plt.pie(values, labels=label, autopct='%.1f%%')
plt.legend(loc=2)
plt.show()
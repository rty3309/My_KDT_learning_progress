# 유동인구가 10만명 이상인 최대 유임 승차 인원이 있는 역은?

import csv

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
max_rate=0
rate=0
max_row=[]
max_total_num=0
fee=4; free=6    # 유임승차 및 무임승차 인덱스

for row in data:
    row[fee]=int(row[fee])
    row[free]=int(row[free])
    total_count=row[fee]+row[free]    # 유임승차수 + 무임승차수

    if (row[free] != 0) and (total_count >= 100000):    # 유동인구 10만명 이상
        rate = row[fee] / total_count    # => 유임승차 비율
        if rate > max_rate:
            max_rate=rate
            max_row=row
            max_total_num=total_count
            print(f'{max_row[1]} {max_row[3]} 전체인원: {max_total_num:,}명 ',
                  f'유임승차인원: {max_row[4]:,}명 ',
                  f'유임승차 비율: {round(max_rate*100,1):,}%')

print('-'*80)
print('최대 유임 승차역')
print(f'{max_row[1]} {max_row[3]} 전체 인원: {max_total_num:,}명 ',
      f'유임승차인원: {max_row[fee]:,}명 ',
      f'유임승차 비율: {round(max_rate*100,1):,}%')
            
f.close()
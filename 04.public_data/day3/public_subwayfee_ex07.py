# 유/무임 승하차 인원이 가장 많은 역은?

import csv

max = [0]*4    # [0]:최대유임승차, [1]:최대유임하차, [2]:최대무임승차, [3]:최대무임하차
max_station=['']*4
label=['유임승차','유임하차','무임승차','무임하차']

# with구문 : 자동으로 파일을 close()시킴
with open('subwayfee.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):    # i = 4,5,6,7
            row[i]=int(row[i])    # [i-4] = 0,1,2,3
            if row[i] > max[i-4]:    # 원본데이터의 컬럼([인덱스]-4) -> max 리스트의 인덱스
                max[i-4] = row[i]
                max_station[i-4] = row[3] + '' + row[1]    # '역이름 지하철노선' 추가
                # 이렇게 안하면(max리스트로 만들어서 저장) 변수 4개 써야 함

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')
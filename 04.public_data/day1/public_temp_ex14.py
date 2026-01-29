# 매년 특정 날짜의 최고 기온 찾기

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_graph_on_date(month, day):
    f=open('daegu-utf8.csv', encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    result=[]
    for row in data:
        if row[-1] != '':
            date_string=row[0].split('-')    # 날짜 정보를 분리하여 해당 날짜에 해당되는 데이터만 리스트에 저장
            if date_string[1] == month and date_string[2] == day:
                result.append(float(row[-1]))    # 최고 기온을 실수형으로 변환 수 리스트에 추가

    f.close()
    plt.figure(figsize=(15,2))
    plt.plot(result, 'royalblue')
    plt.rc('axes', unicode_minus=False)
    plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
    plt.show()

month, date = input('날짜(월 일)을 입력하세요: ').split()    # 입력된 문자열을 공백을 기준으로 분리해서 변수에 입력
draw_graph_on_date(month, date)
# 2000년 이후 특정일의 최저, 최고 기온 찾기

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def draw_lowhigh_graph(start_year, month, day):
    f=open('daegu-utf8.csv', encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    high_temp = []    # 최고 기온을 저장할 리스트
    low_temp = []    # 최저 기온을 저장할 리스트
    x_year = []    # x축 연도를 저장할 리스트
    for row in data:
        if row[-1] != '' and row[-2] != '':
            date_string = row[0].split('-')    # 날짜 데이터를 미리 분리함
            if int(date_string[0]) >= start_year:    # 연도 비교: 문자열 값을 int형으로 변환해서 비교
                if int(date_string[1]) == month and int(date_string[2]) == day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])    # 연도 저장

    f.close()

    plt.figure(figsize=(20,4))
    plt.plot(x_year, high_temp, 'hotpink', marker='o', label='최고기온')    # 최고 기온 그래프
    plt.plot(x_year, low_temp, 'royalblue', marker='s', label='최저기온')    # 최저 기온 그래프

    '''
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic', size=8)    # 간단히 맑은 고딕으로 설정
    else:
        plt.rc('font', family='AppleGothic', size=8)
    '''
    # 이 부분은 koreanize import 해왔으면 안 써도 됨

    plt.rcParams['axes.unicode_minus']=False
    plt.title(f'{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프', size=16)

    plt.legend(loc=2)
    plt.xlabel('Year')
    plt.ylabel('temperature')
    plt.show()

year, month, day = input('연 월 일을 입력하세요: ').split()
draw_lowhigh_graph(int(year), int(month), int(day))
# 공공데이터 과제 #1

# 1. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 
#    최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현하세요.

import csv
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_two_plots(title, x_data, min_temp_list, label_y1, max_temp_list, label_y2):

    plt.rcParams['axes.unicode_minus']=False
    plt.figure(figsize=(10,4))
    plt.plot(x_data, min_temp_list, marker='s', markersize=6, color='b', label=label_y1)
    plt.plot(x_data, max_temp_list, marker='s', markersize=6, color='r', label=label_y2)
    plt.xticks(x_data)

    #plt.ylim(10,40)
    plt.title(title)
    plt.legend()
    plt.show()

def main():
    start_year = int(input('시작 연도를 입력하세요 : '))
    end_year = int(input('마지막 연도를 입력하세요 : '))
    search_month = int(input('기온 변화를 측정할 달을 입력하세요 : '))

    weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
    
    terms = int(end_year - start_year + 1)
    min_temp_list = [0] * terms
    max_temp_list = [0] * terms

    for year in range(terms):
        min_temp = weather_df[(weather_df['날짜'].dt.year == start_year + year) &
                                     (weather_df['날짜'].dt.month == search_month)]
        min_temp_list[year] = float(round(min_temp['최저기온'].mean(),1))    # float()을 씌워줘서 실수로 출력되게 
        
        max_temp = weather_df[(weather_df['날짜'].dt.year == start_year + year) &
                                      (weather_df['날짜'].dt.month == search_month)]
        max_temp_list[year] = round(max_temp['최고기온'].mean(),1).tolist()
        # tolist()로 리스트로 바꾸면서 내부의 값을 가장 가까운 파이썬 표준타입(float)로 변환해서 출력
        # 2가지 방법이 가능하다. tolist()는 판다스에도 있어서 numpy를 import 안해도 사용 가능

    print(f'{start_year}년부터 {end_year}년까지 {search_month}월의 기온 변화')
    print(f'{search_month}월 최저기온 평균 : {min_temp_list}')
    print(f'{search_month}월 최고기온 평균 : {max_temp_list}')
    
    x_data = list(range(start_year, end_year + 1))
    draw_two_plots(f'{start_year}년부터 {end_year}년까지 {search_month}월의 기온 변화', x_data,
                   min_temp_list, '최저기온', max_temp_list, '최고기온')

main()
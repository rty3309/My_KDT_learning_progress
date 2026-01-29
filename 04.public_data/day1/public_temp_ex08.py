# 대구 최저, 최고 기온 날짜와 온도 구하기 예제: Numpy 사용

import csv
import numpy as np

# 이 방법은 데이터를 많이 사용하는 방법임
def get_lowhigh_numpy(data):
    next(data)

    min_temp_list = list()    # 최저 기온 값 저장 리스트
    max_temp_list = list()    # 최고 기온 값 저장 리스트
    date_list = list()    # 날짜 정보 저장 리스트

    for row in data:
        if row[3] == '':
            row[3] = 100
        
        if row[4] == '':
            row[4] = -999
        
        min_temp_list.append(row[3])    # 최저 기온 값을 리스트에 저장
        max_temp_list.append(row[4])    # 최고 기온 값을 리스트에 저장
        date_list.append(row[0])    # 날짜 정보 저장

    max_temp_array = np.array(max_temp_list)    # max_temp_list : 문자열 저장, 리스트를 ndarray로 변경
    max_temp_array = max_temp_array.astype(float)    # 문자열 형태를 float으로 변경
    max_temp = max_temp_array.max()    # 최대값 리턴
    max_index = max_temp_array.argmax()    # 최대값의 인덱스 리턴

    # ndarray : numpy의 핵심인 다차원 행렬 자료구조 클래스
    #           파이썬이 제공하는 list 자료형과 동일한 출력 형태
    min_temp_array = np.array(min_temp_list)    # 리스트를 ndarray로 변경
    min_temp_array = min_temp_array.astype(float)
    min_temp = min_temp_array.min()
    min_index = min_temp_array.argmin()

    print(f'대구 최저 기온 날짜: {date_list[min_index]}, 온도: {min_temp}')
    print(f'대구 최고 기온 날짜: {date_list[max_index]}, 온도: {max_temp}')

def main():
    f = open('daegu-utf8.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(f)
    get_lowhigh_numpy(data)
    f.close()
main()
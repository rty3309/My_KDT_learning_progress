# 대구 최저, 최고 기온 날짜와 온도 구하기 예제

import csv

def get_lowhigh_temp(data):    # csv reader 객체
    '''
        최고 기온 및 최고 기온의 날짜 구하기
    '''
    header=next(data)

    # 상식적으로 안되는 값을 넣어서 초기값 지정
    lowest_temp=100    # 최저 기온 값을 저장할 변수 초기화(가장 큰 값)
    lowest_date=''    # 최저 기온의 날짜를 저장할 변수 초기화

    highest_temp=-999    # 최고 기온을 저장할 변수 초기화(가장 작은 값)
    highest_date=''    # 최고 기온의 날짜를 저장할 변수 초기화

    for row in data:
        if row[3] == '':
            row[3] = lowest_temp
        row[3] = float(row[3])
        # csv 파일 데이터는 문자열로 취급, 산술 연산을 위해 실수형(float)으로 변환

        if row[4] =='':
            row[4] = highest_temp
        row[4] = float(row[4])

        # 최저 기온 계산(최저 기온 값 업데이트)
        if row[3] < lowest_temp:
            lowest_temp = row[3]
            lowest_date = row[0]

        # 최고 기온 계산(최고 기온값 업데이트)
        if row[4] > highest_temp:
            highest_temp = row[4]
            highest_date = row[0]    # 날짜 : index[0]
    print('-'*50)
    print(f'대구 최저 기온 날짜: {lowest_date}, 온도: {lowest_temp}')
    print(f'대구 최고 기온 날짜: {highest_date}, 온도: {highest_temp}')

def main():
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_lowhigh_temp(data)
    f.close()

main()
# 이렇게 계산하면 판다스보다 메모리 훨씬 적게 사용함
# 판다스는 데이터 전체를 불러와서 처리하므로
# CSV 파일에서 데이터 읽어 오기

import csv

f = open('daegu.csv', 'r', encoding='utf-8')

data = csv.reader(f, delimiter=',')    # ',' : 파일 내부의 구분자
# csv 파일 중에 구분자가 탭으로 된 경우도 있음. 그 때는 ',' 대신 탭 써주면 됨
print(data)    # csv_reader 객체 출력

f.close()    # 파일 닫기

# 결과는 터미널에 <_csv.reader object at 0x00000161E2B34520> 이런 식으로 출력됨.
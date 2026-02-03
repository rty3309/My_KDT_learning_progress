# 미세먼지 데이터 확인

import pandas as pd
from tabulate import tabulate

# 미세먼지 데이터 분석
# dust.xlsx 불러오기
dust=pd.read_excel('dust.xlsx')
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))


# 미세먼지 데이터 확인 
# 미세먼지 데이터 구조 확인
print('\n')
print(dust.info())


# 미세먼지 데이터 전처리 : 컬럼이름 변경
# 한글 컬럼명을 영문으로 변경
print('\n')
dust.rename(columns={'날짜':'date', '아황산가스':'so2',
                     '일산화탄소':'co', '오존':'o3',
                     '일산화질소':'no2'}, inplace=True)
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))


# 미세먼지 데이터 전처리 : ['date'] 컬럼을 datetime으로 변경
# ['date'] 컬럼의 자료형을 datetime으로 변경하기
print('\n')
print('[date] 자료형(object)을 datetime 타입으로 변경')
dust['date']=pd.to_datetime(dust['date'], format='%Y-%m-%d %H')
# format='%Y-%m-%d %H' 은 실제 원본 엑셀파일의 형태
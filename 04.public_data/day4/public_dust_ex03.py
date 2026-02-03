# 미세먼지 데이터 전처리 : 누락값(결측치) 확인

import pandas as pd
from tabulate import tabulate

dust=pd.read_excel('dust_hour.xlsx')
print('결측치 개수 확인하기')
print(dust.isna().sum())    # isnull() 동일

# 미세먼지 데이터에서 결측치를 포함하는 행 출력하기
print('결측치를 포함한 데이터 출력')
print(dust[dust.isna().any(axis=1)])    # NaN 값을 포함하는 행 출력


# 미세먼지 데이터 전처리 : 결측치 채우기
# 결측치 채우기
print('\n')
print('결측치 채우기')
dust.ffill(inplace=True)    # Pandas 2.2.0 이후
print(dust.isnull().sum())
# 이전 결측치의 index를 다시 출력해서 확인
print(dust.iloc[110:112])    # 이전 결측치 index


# 날씨 데이터 읽기 및 확인
print('\n')
weather=pd.read_excel('weather.xlsx')
print(tabulate(weather.head(), headers='keys', tablefmt='psql'))


# 날씨 데이터 기본 정보 출력
print('\n')
print(weather.info())


# 날씨 데이터 전처리 : 컬럼 삭제 및 컬럼 이름 변경
print('\n')
weather.drop(['지점','지점명'], axis=1, inplace=True)
weather.columns = ['date', 'temp', 'wind', 'rain', 'humidity']
print(tabulate(weather.head(), headers='keys', tablefmt='psql'))


# 날씨 데이터 전처리 : 결측치 확인
print('\n')
print('날씨 데이터 결측치 개수 확인하기')
print(weather.isna().sum())
# 날씨 데이터에서 결측치를 포함하는 행 출력하기 : 현재 결측치 없음
print('날씨 데이터에서 결측치를 포함하는 행 출력 ')
print(weather[weather.isna().any(axis=1)])


# 강수량 데이터 변경
print('\n')
print('강수량이 0인 항목을 0.01로 변경')
weather['rain']=weather['rain'].replace(0,0.01)
print(weather['rain'].value_counts())


# 두 데이터의 크기 확인
print('\n')
print('dust, weather의 크기 확인')
print('dust.shape', dust.shape)
print('weather.shape', weather.shape)


# 미세먼지 데이터와 날씨 데이터 병합
print('\n')
print('dust_hour와 weather 데이터 병합')
merged_df = pd.merge(dust, weather, how='inner', on='date')
print(tabulate(merged_df.head(), headers='keys', tablefmt='psql'))
# 병합된 데이터프레임(merged_df)의 크기 확인
print(merged_df.shape)


#병합된 데이터프레임을 엑셀 파일로 저장 : 검증 용도
print('\n')
merged_df.to_excel('dust_weather.xlsx', index=False)


# 데이터 분석 : 모든 요소별 상관관계 확인
print('\n')
print(tabulate(merged_df.corr(), headers='keys', tablefmt='psql'))


# 데이터 분석 : 미세먼지(PM10)과 상관 관계
print('\n')
print('미세먼지(PM10)과의 상관관계 분석')
corr=merged_df.corr()
print(corr['PM10'].sort_values(ascending=False))    # 내림차순 정렬
print('초미세먼지(PM2.5)와 상관관계 분석')
print(corr['PM2.5'].sort_values(ascending=False))    # 내림차순 정렬
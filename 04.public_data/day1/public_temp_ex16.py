# Pandas를 활용한 기온 데이터

# (1) Pandas의 read_csv() 함수 호출
import pandas as pd

weather_df = pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)    # 날짜 컬럼은 object(문자열) 타입

# (2) DataFrame의 column 이름 변경: 특수 문자(최고기온(℃)) 제거
weather_df.columns=['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

# (3) [‘날짜’] 컬럼의 데이터 타입을 datetime 타입으로 변경
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
print(weather_df['날짜'].dtype)

# (4) 결측치(누락값: missing data) 개수 구하기
print(weather_df.head(5))
print(weather_df.shape)
num_rows = weather_df.shape[0]    # shape(row, col), shape[0]: row의 개수
num_missing = num_rows - weather_df.count()    # df.count() : 정상값의 개수. # 전체행 - 정상값을 가지는 행
print(num_missing)

# (5) 결측치(NaN) 처리
# dropna(axis) : 결측치 제거
# fillna(0) : 결측치를 0으로 변경
# ffill() : 이전 값으로 변경
# bfill() : 이후 값으로 변경
# interpolate(): 결측치 양쪽의 값으로 중간값 계산
weather_df = weather_df.dropna(axis=0)
print(weather_df.count())
print(weather_df.head(5))

# (6) 결측치를 제거한 최종 데이터를 csv파일로 저장
weather_df.to_csv('daegu-utf8-df.csv', index=False, mode='w', encoding='utf-8-sig')

# (7) 특정 연도와 달의 최고, 최저 기온 평균값 계산
print('특정 연도와 달의 최고, 최저 기온 평균값 계산')

year_df = weather_df[weather_df['날짜'].dt.year == 2024]    # weather_df['날짜'].dt.year == 2024 : 검색조건
month_df = year_df[year_df['날짜'].dt.month == 8]
print(month_df.head())

# (8) 특정 연도와 달의 최저 기온 및 최고 기온의 평균 계산
max_tamp_mean = round(month_df['최고기온'].mean(),1)
min_temp_mean = round(month_df['최저기온'].mean(),1)

print(f'2024년 8월 최저기온 평균: {min_temp_mean}, 최고기온 평균: {max_tamp_mean}')
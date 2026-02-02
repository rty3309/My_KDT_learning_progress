# 지하철 시간대별 이용 현황: 엑셀 파일 및 Pandas 활용

# 1) 출퇴근 시간대 이용 현황
import pandas as pd
from tabulate import tabulate
# import tabulate 안 하고 위 처럼 쓰는 이유 : 
# import tabulate만 해도 작동은 하지만, 매번 tabulate.tabulate()라고 
# 쓰는 게 귀찮고 코드가 지저분해 보이기 때문에 from ... import ... 방식을 주로 사용

print('1) 출퇴근 시간대 이용 현황')
# 지하철 시간대별 이용현황
df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])    # multi-index 형태 header=[0,1] 추가
print(df.head())

# 2) 모든 컬럼 내용 확인
print('\n')
print('2) 모든 컬럼 내용 확인')
print(df.columns)

# 3) 특정 컬럼 데이터 가져오기 : 호선명
print('\n')
print('3) 특정 컬럼 데이터 가져오기 : 호선명')
print(df[('호선명', 'Unnamed: 1_level_1')])

# 4) 특정 컬럼 데이터 가져오기 : 지하철역
print('\n')
print('4) 특정 컬럼 데이터 가져오기 : 지하철역')
print(df[('지하철역', 'Unnamed: 3_level_1')])

# 5) DataFrame에서 여러 컬럼 선택
print('\n')
print('5) DataFrame에서 여러 컬럼 선택')
commute_time_df = df.iloc[:, [1,3,10,12,14]]
print(tabulate(commute_time_df.head(), headers='keys', tablefmt='psql'))

# 6) 모든 컬럼의 데이터 타입 확인
print('\n')
print('6) 모든 컬럼의 데이터 타입 확인')
print(commute_time_df.dtypes)

# 7) 천 단위 콤마 제거
print('\n')
print('7) 천 단위 콤마 제거')
cols = [('07:00:00~07:59:59', '승차'), ('08:00:00~08:59:59', '승차'), ('09:00:00~09:59:59', '승차')]
commute_time_df.loc[:, cols] = commute_time_df.loc[:, cols].map(lambda x: x.replace(',',''))
print(tabulate(commute_time_df.head(), headers='keys', tablefmt='psql'))

# 8) 데이터 타입 변경 : object에서 int64로 변경
print('\n')
print('8) 데이터 타입 변경: object에서 int64로 변경')
commute_time_df = commute_time_df.astype({col: 'int64' for col in cols})
print(commute_time_df.dtypes)

# 9) 각 행(지하철 역)의 승차 인원 수 합 계산
print('\n')
print('9) 각 행(지하철 역)의 승차 인원 수 합 계산')
row_sum_series = commute_time_df.sum(axis=1, numeric_only=True)    # 숫자만 있는 열들만 가져와서 더하기
passenger_number_list=row_sum_series.to_list()
print(row_sum_series)

# 10) 최대값 및 최대값 인덱스 찾기
print('\n')
print('10) 최대값 및 최대값 인덱스 찾기')
max_number = row_sum_series.max()    # 해당 열에서 최대값 찾기
print(max_number)
max_index = row_sum_series.idxmax()
max_line, max_station = commute_time_df.iloc[max_index, [0,1]]    # 최대값의 [0]:호선, [1]:지하철역명
print(f'출근 시간대 최대 승차 인원역: {max_line} {max_station} {max_number:,}명')

# 11) bar-chart 그리기
print('\n')
print('11) bar-chart 그리기')
import matplotlib.pyplot as plt

passenger_number_list.sort(reverse=True)
plt.figure(dpi=100)
plt.bar(range(len(passenger_number_list)), passenger_number_list)
plt.show()
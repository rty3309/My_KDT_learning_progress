# 1월과 8월의 기온 데이터 히스토그램

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f=open('daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug=[]
jan=[]

for row in data:
    if row[0] != '' and row[4] != '':
        month = row[0].split('-')[1]    # ['2024', '01', '01'], 첫번째 '01' : 월[1]
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

f.close()
plt.hist(aug, bins=100, color='tomato', label='Aug')
plt.hist(jan, bins=100, color='b', label='Jan')
plt.xlabel('Temperature')
plt.rc('axes', unicode_minus=False)    # 레이블에 '-' 부호가 깨지는 현상 방지
plt.title('대구 1월과 8월의 최고 기온')
plt.legend()
plt.show()
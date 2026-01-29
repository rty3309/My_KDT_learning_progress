# 기온 히스토그램(8월)

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug=[]

for row in data:
    if row[0] != '' and row[4] !='':
        month = row[0].split('-')[1]    # 날짜정보: 2024-08-10에서 ('-')을 기준으로 분리함, 인덱스 [0]: 2024, [1]: 08(8월만 검사함), [2]: 10
        if month == '08':    # 문자열 비교(하드코딩)
            aug.append(float(row[-1]))

f.close()

plt.hist(aug, bins=100, color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel('Temperature')    # x축 레이블
plt.ylabel('Counts')    # y축 레이블
plt.show()
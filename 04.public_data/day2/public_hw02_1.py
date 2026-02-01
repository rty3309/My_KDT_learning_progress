# 공공데이터 과제 #2

# 대구광역시 전체 및 9개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 
# 달성군, 군위군) 남녀 비율을 각각의 파이 차트로 구현하세요.

import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f=open('gender.csv', encoding='euc_kr')
data=csv.reader(f)
population=[]
city= '대구광역시'
male_count=0
female_count=0
gus = []
male_pops = []
female_pops =[]

def parse_district_name(city):
    city_name = re.split('[()]', city)
    #print(city_name)
    return city_name[0]

for row in data:
    if city in row[0]:
        daegu = parse_district_name(row[0])
        male_count = int(row[104].replace(',',''))
        female_count = int(row[207].replace(',',''))
        print(f'{daegu}: (남:{male_count:,} 여:{female_count:,})')
        gus.append(daegu)
        male_pops.append(male_count)
        female_pops.append(female_count)

fig, axes= plt.subplots(2,5,figsize=(4,8))
fig.suptitle(city + ' 구/군별 남녀 인구 비율')
color = ['cornflowerblue', 'tomato']
num=0

for i in range(2):
    for j in range(5):
        population = [male_pops[num], female_pops[num]]
        axes[i,j].pie(population, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
        axes[i,j].set_title(gus[num])
        num += 1
plt.show()
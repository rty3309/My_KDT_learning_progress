# 공공데이터 과제 #2

# 대한민국 전체 행정구역중에서 고령화지수가 가장 높은 지역의 이름과 고령인구,
# 유소년인구 수, 고령화지수를 화면에 출력하고 유소년인구수와 고령인구수 비율을
# 파이차트로 작성하시오.


import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f = open('age.csv', encoding='euc_kr')
data = csv.reader(f)
next(data)
location = ''
max_aging_ratio = 0

def draw_pie_chart(old_city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%',
            startangle=90, colors=plt.cm.Paired.colors, textprops={'fontsize':8})
    plt.legend(loc=1)
    plt.title(old_city + ' 고령화 비율')
    plt.show()

def parse_district_name(city):
    '''
    '행정구역' 명칭에서 숫자 부분을 제거함
    - 서울특별시 종로구 (1111000000)
    '''
    city_name = re.split('[()]', city)
    #print(city_name)
    return city_name[0]

def get_age_population(row, start_age, end_age):
    '''
    age.csv 파일에서 나이를 이용한 인구수 구하기
    - 나이를 해당 인덱스로 변환 : 인덱스 = 나이 + 3
    '''
    poplation = 0
    start_index = start_age + 3
    end_index = end_age + 3

    for num in row[start_index:end_index+1]:
        num = num.replace(',','')
        num = int(num)
        poplation += num
    return poplation

def get_aging_population():
    youth_range = (0,14)    # 0세 ~ 14세까지
    old_range = (65,100)    # 65세 ~ 100세 이상
    old_population = 0
    youth_population = 0
    label_list = ['유소년 인구', '고령인구']
    max_aging_ratio = 0
    old_city = ''
    old_youth_pop = 0
    old_old_pop = 0

    for row in data:
        location = parse_district_name(row[0])
        youth_population = get_age_population(row, youth_range[0], youth_range[1])
        old_population = get_age_population(row, old_range[0], old_range[1])
        if youth_population == 0:
            continue    # 0으로 나누기 멈춰!         
        aging_rate = round((old_population*100)/youth_population, 1)
        if aging_rate > max_aging_ratio:
            max_aging_ratio = aging_rate
            old_city = location
            old_youth_pop = youth_population
            old_old_pop = old_population

    print(f'{old_city} 고령인구 : {old_old_pop:,}명,',
          f'유소년인구 : {old_youth_pop:,}명,',
          f'노령화지수 : {max_aging_ratio}%')
    
    draw_pie_chart(old_city, [old_youth_pop, old_old_pop], label_list)

get_aging_population()
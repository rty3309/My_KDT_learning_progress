# 학령 인구 비율 분석(초등학생~대학생)

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_pie_chart(city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%',
            startangle=90, colors=plt.cm.Pastel1.colors, textprops={'fontsize':8})
    plt.legend()
    plt.title(city + '학령인구 비율')
    plt.show()

def get_age_population(row, start_age, end_age):
    '''
    age.csv 파일에서 나이를 이용한 인구수 구하기
    - 나이를 해당 인덱스로 변환 : 인덱스 = 나이 + 3
    '''
    population=0
    start_index= start_age+3
    end_index=end_age+3

    for num in row[start_index: end_index+1]:
        num = num.replace(',','')
        num = int(num)
        population += num

    return population

def school_age_population(city):
    city_population = 0
    non_school_pop = 0
    school_age_pop = 0

    label_list = ['초등학생','중학생','고등학생','대학생','비학령인구']
    population_list = []

    f=open('age.csv', encoding='euc_kr')
    data=csv.reader(f)
    header=next(data)

    for row in data:
        if city in row[0]:
            city_population = row[1]
            city_population = city_population.replace(',','')
            city_population = int(city_population)

            # 초등학생 인구 계산 : 6세[9] ~ 11세[14]
            elementary_pop = get_age_population(row,6,11)
            population_list.append(elementary_pop)

            # 중학생 인구 계산 : 12세[15] ~ 14세[17]
            middleschool_pop = get_age_population(row, 12,14)
            population_list.append(middleschool_pop)

            # 고등학생 인구 계산 : 15세[18] ~ 17세[20]
            highschool_pop = get_age_population(row,15,17)
            population_list.append(highschool_pop)

            # 대학생 인구 계산 : 18세[21] ~ 21세[24]
            university_pop = get_age_population(row,18,21)
            population_list.append(university_pop)

            school_age_pop = (elementary_pop+middleschool_pop+highschool_pop+university_pop)

            # 비학령 인구 계산
            non_school_pop = city_population - school_age_pop
            population_list.append(non_school_pop)
            break

    school_age_pop_rate = round((school_age_pop*100)/city_population,1)

    print(f'전체 인구수 : {city_population}:,',
          f'학령 인구수 : {school_age_pop}:,',
          f'학령 인구 비율 : {school_age_pop_rate}%')
    
    draw_pie_chart(city, population_list, label_list)

city = input('학령인구를 분석할 도시 이름 : ')
school_age_population(city)
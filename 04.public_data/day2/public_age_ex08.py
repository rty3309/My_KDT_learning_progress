# 노령화 지수 계산 예제

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_pie_chart(city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%',
            startangle=90, colors=plt.cm.Pastel1.colors, textprops={'fontsize':8})
    plt.legend(loc=1)
    plt.title(city + '고령화 지수')
    plt.show()

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

def get_aging_population(city):
    youth_range = (0,14)    # 0세 ~ 14세까지
    old_range = (65,100)    # 65세 ~ 100세 이상
    old_population = 0
    youth_population = 0
    label_list = ['유소년 인구', '고령인구']

    f = open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    next(data)    # 헤더 정보 건너뜀

    for row in data:
        if city in row[0]:
            youth_population = get_age_population(row, youth_range[0], youth_range[1])
            old_population = get_age_population(row, old_range[0], old_range[1])
            break
    
    aging_rate = round((old_population*100)/youth_population, 1)
    print(f'{city} 고령인구 : {old_population:,}명,',
          f'유소년인구 : {youth_population:,}명,',
          f'노령화지수 : {aging_rate}%')
    
    draw_pie_chart(city, [youth_population, old_population], label_list)

city = input('노령화 지수를 분석할 도시 이름 : ')
get_aging_population(city)
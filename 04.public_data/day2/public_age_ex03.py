# 대구시 산격3동의 인구 분포 그래프 그리기

import csv
import matplotlib.pyplot as plt
import re    # regex(Regular Expression(정규 표현식)) 모듈, 크롤링 가면 하루종일 쓸 예정
import koreanize_matplotlib

f=open('age.csv', encoding='euc-kr')
data=csv.reader(f)
result=[]
city=''

for row in data:
    if '산격3' in row[0]:    # # [()] 안의 괄호()가 구분자
        # 정규식(re) : 여러 구분자 사용 가능
        str_list = re.split('[()]', row[0])    # row[0] : '대구광역시 북구 산격3동(2723063000)'
        print(str_list)
        city=str_list[0]
        for city_data in row[3:]:    # 0세부터 100세 이상까지 데이터 
            city_data = city_data.replace(',', '')    # 천 단위 콤마 삭제
            result.append(int(city_data))    # 문자열을 숫자로 변환

f.close()
print(result)
plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()
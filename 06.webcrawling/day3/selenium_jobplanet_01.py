"""
잡플래닛 회사 평점 크롤링
- 전체 평점
- 복지 및 급여
- 업무와 삶의 균형 등

회사명: class=name

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys  import Keys
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

company_dict = {'삼성전자':'https://www.jobplanet.co.kr/companies/30139/reviews/삼성전자',
                 'LG전자':'https://www.jobplanet.co.kr/companies/19514/reviews/lg전자',
                 'SK하이닉스':'https://www.jobplanet.co.kr/companies/20561/reviews/에스케이하이닉스',
                 '네이버':'https://www.jobplanet.co.kr/companies/42217/reviews/네이버'}

user_id = 'your id'
passwd = 'password'

def  login(driver,  user_id,  pwd):
    driver.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")
    time.sleep(1)

    # 아이디 입력
    login_id  =  driver.find_element(By.ID,  "user_email")
    login_id.send_keys(user_id)

    # 비밀번호 입력
    login_pwd  =  driver.find_element(By.ID,  "user_password")
    login_pwd.send_keys(pwd)

    # 로그인 버튼 클릭
    login_id.send_keys(Keys.RETURN)
    time.sleep(5)


def get_review_score(driver):    
    compary_score_dict = {} # {'삼성전자': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]}  형태
    for company_name in company_dict.keys():
        score_title_list = [] # 평점 이름(전체평점, 복지/급여, 워라벨, 사내문화, ...)
        score_list = []
        
        company_url = company_dict.get(company_name)
        driver.get(company_url)
        time.sleep(2)
        
        print(company_name)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        total_score = soup.select_one('span.rate_point').text
        score_title_list.append('전체 평점')
        score_list.append(float(total_score))

        # 세부 평점 
        rate_bar_group = soup.select_one('div.rate_bar_group')
        
        # 평점 문자열 (복지/급여, 워라벨, 사내문화, 승진기회, 경영진)
        point_title_list = rate_bar_group.select('div.rate_bar_title')
        for title in point_title_list:
            score_title_list.append(title.text)
        
        # 문자열 형태의 평점 정보 
        txt_point_list = rate_bar_group.select('span.txt_point')
        for point in txt_point_list:            
            score_list.append(float(point.text)) # 실수로 변경 
 
        # 각 회사별 평점 이름: 평점 출력 
        for title, score in zip(score_title_list, score_list):
            print(f'{title}: {score}', end=' ')
        print()
        print('-' * 85)

        # 딕셔너리에 {'회사명': [3.8, 4.2, ...]} 형태로 저장 모든 평점 추가하기
        compary_score_dict[company_name] = score_list

    print('company_score_dict')
    for key in compary_score_dict.keys():
        print(f'{key}: {compary_score_dict.get(key)}')

    # 딕셔너리를 DataFrame으로 변환
    # orient='index': 딕셔너리의 키가 행의 색인이 되고
    # 딕셔너리의 값이 행의 데이터가 됨
    #columns = ['전체평점', '복지/급여', '워라벨', '사내문화', '승진 기회', '경영진']
    company_score_df = pd.DataFrame.from_dict(compary_score_dict,
                                            orient='index', 
                                            columns=score_title_list)

    print(tabulate(company_score_df, headers='keys', tablefmt='psql'))
    #company_score_df.to_excel('company_scores.xlsx', index=False)
    file_name = 'company_scores.csv'
    company_score_df.to_csv(file_name, index=True, mode='w', encoding='utf-8-sig')
    print(f'{file_name} saved')
    

def main():
    driver = webdriver.Chrome()

    #login(driver, user_id, passwd)
    get_review_score(driver)

    time.sleep(5)
    driver.close()


main()


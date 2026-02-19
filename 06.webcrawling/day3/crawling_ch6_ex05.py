# Selenium API #4 : 프레임 이동 예제

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame')    # 해당 iframe으로 이동

html = driver.page_source    # 전체 HTML 소스를 가져옴
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all('div', {'class':'se-module'})

result1=[]
for result in results:
    remove_carriage_str = result.text.replace('\n', '')
    print(remove_carriage_str)
    result1.append(remove_carriage_str) 
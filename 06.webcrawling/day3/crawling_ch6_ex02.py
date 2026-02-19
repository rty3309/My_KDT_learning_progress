# Selenium API : element 접근 예제

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)    # 없어도 됨. 페이지가 로딩될 때 까지 5초를 기다리겠다는 의미.

# find_element(By.CLASS_NAME, '클래스이름'): 하나의 클래스 이름 선택
name = driver.find_element(By.CLASS_NAME, 'green')
print(name.text)

print('-'*20)

# find elements(By.CLASS_NAME, '클래스이름'): 해당 클래스 이름을 모두 검색
name_list = driver.find_elements(By.CLASS_NAME, 'green')    # 클래스 속성값이 'green' 모두 검색
for name in name_list:
    print(name.text)
time.sleep(3)
driver.quit()
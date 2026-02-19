# Selenium 사용

from selenium import webdriver
import time
'''
selenium 4.xx 버전은 chromedriver를 별도로 다운로드할 필요 없음
'''
driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

print(f'title:{driver.title}')
print(driver.page_source)    # HTML 전체 소스가 저장되어 있음
time.sleep(10)
driver.quit()
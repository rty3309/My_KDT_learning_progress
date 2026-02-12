# BeautifulSoup 객체 생성 예제 1

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.naver.com')
soup = BeautifulSoup(html, 'html.parser')
print(soup.find('h1'))    # h1 태그 예시 추출
# CSS 속성을 이용한 검색
# CSS 속성을 이용한 태그 검색(등장 인물 검색)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, "html.parser")

# 등장인물의 이름 : 녹색
name_list=soup.find_all('span', {'class': 'green'})
for name in name_list:
    print(name.text)
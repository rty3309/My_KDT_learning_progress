# Beautiful 객체 생성 예제 3
# 방법 3 : html 파일 읽기

from bs4 import BeautifulSoup

with open('hello.html', 'r', encoding='utf-8') as f:
    html = f.read()    # 텍스트 전체를 하나의 문자열로 읽음

soup = BeautifulSoup(html, 'html.parser')
# 파일 내 title 태그 텍스트 출력
print(soup.title.string)
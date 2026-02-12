# BeautifulSoup 객체 생성 예제 2

from bs4 import BeautifulSoup

html ='''
<div>
    <a href="https://www.naver.com">네이버</a>
    <a href="https://www.kakao.com">카카오</a>
</div>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.find('a').text)    # 첫 번째 링크 텍스트 출력 : 네이버
print([a.text for a in soup.find_all('a')])    # 모든 링크 텍스트 출력, 리스트 형태
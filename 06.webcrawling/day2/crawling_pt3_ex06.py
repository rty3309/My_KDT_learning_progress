# 트리 이동 : 형제 다루기 

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

# next_siblings 속성
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*30)

print('\n')
# previous siblings 속성
print('previous_siblings')
for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)

print('\n')
# 문자열 마지막에 whitespace(‘\n’, ‘\r’등)가 있는 경우
sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print('sibling1: ', sibling1)
print(ord(sibling1))    # ord(문자) : 문자의 Unicode 정수를 리턴
print()
# next_sibling.next_sibling 이용
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)

print('\n')
# 트리 이동 : 부모 다루기 1
style_tag = soup.style    # <style> 태그에 직접 접근
print(style_tag.parent)

print('\n')
# 트리 이동 : 부모 다루기 2
img1 = soup.find('img', {'src':'../img/gifts/img1.jpg'})
prev_text = img1.parent.previous_sibling.text
print(prev_text)
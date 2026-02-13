# CSS 속성을 이용한 검색
# 속성 사용

from bs4 import BeautifulSoup

html_text='<span class="red">Heavens! what a virulent attack!</span>'

soup=BeautifulSoup(html_text, 'html.parser')

span_tag = soup.find('span')
print('span_tag: ', span_tag)
print('attrs: ', span_tag.attrs)
print('value: ', span_tag.attrs['class'])
print('text: ', span_tag.text)
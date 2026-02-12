# BeautifulSoup 기초 : find() 함수

html_example='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link external_link2" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

print(soup.find('div'))

print('\n')
# 여러 <div> 태그 중 특정 속성을 가지는 항목 추출
print(soup.find('div', {'id':'text_id2'}))

print('\n')
# .string, .text 또는 get_text()
div_text = soup.find('div', {'id':'text_id2'})
print(div_text.text)
# '\n   Example page\n  <p>g</p>\n'
print(div_text.string)    # None 리턴

print('\n')
# <a>태그 중 class 속성의 속성값이 “internal_link”인 정보 추출 {‘class’:’internal_link’}
href_link = soup.find('a', {'class': 'internal_link'})    # 딕셔너리 형태
href_link = soup.find('a', class_ = 'internal_link')    # class_ 사용 : class는 파이썬 예약어라서

print(href_link)    # <a class="internal_link", ...>
print(href_link['href'])    # <a> 태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href'))    # ['href']와 동일 기능
print(href_link.text)    # <a> Page1 </a> 태그 내부의 텍스트(Page1) 추출

print('\n')
# <a> 태그 내부의 모든 속성 가져오기: attrs
print('href_link.attrs: ', href_link.attrs)    # <a> 태그 내부의 모든 속성 출력
print('class 속성값: ', href_link['class'])    # class 속성의 value 출력

print('values():', href_link.attrs.values())    # 모든 속성들의 값 출력

values = list(href_link.attrs.values())    # dictionary 값들을 리스트로 변경
print(f'values[0] : {values[0]}, values[1] : {values[1]}')

print('\n')
# href 속성의 값이 ‘www.google.com’인 항목 검색
href_value = soup.find(attrs={'href': 'www.google.com'})
href_value = soup.find('a', attrs={'href':'www.google.com'})
# attrs = 생략 가능
print(soup.find('a', {'href':'www.google.com'}))    # soup.find('a', {'href':'www.google.com'})이 가장 일반적인 사용 형태

print('href_value : ', href_value)
print(href_value['href'])
print(href_value.text)

print('\n')
# span 태그의 속성 가져오기
span_tag = soup.find('span')

print(f'span_tag : {span_tag}')
print(f'attrs: {span_tag.attrs}')
print(f'value: {span_tag.attrs['class']}')
print(f'value: {span_tag['class']}')
print(f'text: {span_tag.text}')

print('\n')
# class 속성
print('class 속성값: ', href_link['class'])

# class 속성 예제
from bs4 import BeautifulSoup

tr = '''
<table>
    <tr class="passed a b c" id="rowl example"><td>t1</td></tr>
    <tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):    # find_all('tag') : 해당 tag를 모두 찾아서 리스트로 리턴
    print(row.attrs)
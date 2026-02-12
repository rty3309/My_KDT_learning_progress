# BeautifulSoup 기초 : select_one() 함수

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

head = soup.select_one('head')
print(head)
print('head.text : ', head.text.strip())

h1 = soup.select_one('h1')    # 첫 번째 <h1> 태그 선택
print(h1)

print('\n')
# <h1>태그의 id 검색: #id
# <h1>태그의 id가 "footer"인 항목 추출
footer = soup.select_one('h1#footer')    #  # : id 속성을 의미
print(footer)

class_link = soup.select_one('a.internal_link')    #  . : class 속성을 의미 
print(class_link)

print(class_link.text)
print(class_link['href'])

print('\n')
# 계층적 하위 태그 접근 1
# 계층적 접근
link1=  soup.select_one('div#link > a.external_link')
print(link1)

# find() 함수와 비교 : 범위를 축소해 나감(첫 번 째 검색한 내용에서 다시 검색 시도)
link_food = soup.find('div', {'id':'link'})

external_link = link_food.find('a', {'class':'external_link'})
print('find external_link: ', external_link)

print('\n')
# 계층적 하위 태그 접근 2 : 공백으로 하위 태그 선언
# (상위태그 하위태그) 형식으로 접근: 자손 관계의 하위태그
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.text)

internal_link = soup.select_one('div#link a.internal_link')
print(internal_link['href'])
print(internal_link.text)

print('\n')
# 자손 관계
# <div id=“link”> 와 <p id=“second”>는 자손 관계
link1 = soup.select_one('div#link p#second')
print(f'link1: {link1}')
# 자손 관계는 자식관계(부모 > 자식)로 검색 안됨
link2 = soup.select_one('div#link > p#second')
print(f'link2: {link2}')

print('\n')
# 자식 관계
# <div id=“class1”>과 <p id=“second”>는 자식 관계
link3 = soup.select_one('div#class1 > p#second')
print(f'link3: {link3}')
# 자식 관계는 자손 관계에 포함
link4 = soup.select_one('div#class1 p#second')
print(f'link4: {link4}')

print('\n')
# select() 함수
h1_all = soup.select('h1')
print('h1_all:', h1_all)
# html 문서의 모든 <a> 태그의 href 값 추출
url_links = soup.select('a')
for link in url_links:
    print(link['href'])

print('\n')
# <div id=“class1”> 내부의 모든 <a> 태그 검색 후 url 추출
div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])
#<div id=“class1”> 내부의 모든 <a>태그는 자손 관계 – 공백으로 구분할 수 있음
div_urls2 = soup.select('div#class1 a')
print(div_urls2)

# ** 자식 관계는 자손 관계로 검색 가능함 **

print('\n')
# 여러 항목 검색하기
# <h1 id="heading">과 <h1 id="footer"> 항목 가져오기
h1 = soup.select('#heading, #footer')    # select('#heading', '#footer')로 하면 오류 발생
print(h1)
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)
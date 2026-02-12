# BeautifulSoup 기초 : tag 직접 접근 방법

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
# 객체이름(soup)에는 전체 html 문서가 포함되어 있다.

print(soup.title)    # <titile> 태그 전체를 가져옴
print(soup.title.string)    # <title> 태그의 텍스트만 리턴
print(soup.title.text)    # .string, .get_text()와 동일한 기능

print()
# 태그명.parent : 해당 태그를 포함하고 있는 부모(<head> 태그 출력)
print(soup.title.parent)

print()
# <body> 태그에 직접 접근
print(soup.body)

print()
# <h1> 태그 접근
print(soup.h1)
print(soup.h1.string)

print()
# <a> 태그 접근
print(soup.a)    # <a> 태그 전체를 추출
print(soup.a.string)    # <a> 태그 내부의 텍스트 추출 (google)
print(soup.a['href'])    # <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href'))    # a['href']와 동일 기능
print(soup.a['class'])    # list 타입으로 반환
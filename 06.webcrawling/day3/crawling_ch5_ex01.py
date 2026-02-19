# 네이버 블로그 검색 소스 코드

from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup

query ='ChatGPT'    #query1 = quote('챗지피티')    # 한글 검색어 전달시에는 quote 사용
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'

urlrequest = Request(url, headers={'User-Agent':'Mozilla/5.0'})
html = urlopen(urlrequest)
soup = BeautifulSoup(html, 'html.parser')

blog_titles = soup.select('span.sds-comps-text-type-headline1')    # 블로그 제목
blog_contents = soup.select('span.sds-comps-text-type-body1')    # 블로그 요약 내용

print(f'타이틀 검색 수: {len(blog_titles)}')
print(f'블로그 내용 검색 수: {len(blog_contents)}')
print('-'*80)
for i in range(len(blog_titles)):
    print(f'[{i+1}]: {blog_titles[i]}.text')
    print(f'url: {blog_titles[i].parent['href']}')
    print(f'{blog_contents[i].text}')
    print('-'*80)
# 전체 위키피디아에서 첫 번째 문단 출력

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

pages_set = set()
count = 0

def get_links(page_url):
    global pages_set
    global count

    wiki_url = f'https://en.wikipedia.org{page_url}'
    urlrequest = Request(wiki_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.text) # <h1> 태그 검색
        print(bs.find('div', {'id':'mw-content-text'}).find('p').text)    # 첫 번째 문단 출력
    except AttributeError as e:
        print('this page is missing something! Continuing: ', e)
    
    pattern = '^(/wiki/)((?!:).)*$'
    for link in bs.find_all('a', href=re.compile(pattern)):
        if 'href' in link.attrs and link['href'] not in pages_set:
            new_page = link['href']
            print('-'*40)
            count += 1
            print(f'[{count}]: {new_page}')

            pages_set.add(new_page)
            get_links(new_page)


get_links('')
# Wikipedia 전체 사이트에서 데이터 수집

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
    for link in bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs and link['href'] not in pages_set:
            # set 내부에 해당 link가 없으면 추가
            new_page = link['href']    # 새로운 페이지 발견
            count += 1
            print(f'[{count}]: {new_page}')
            pages_set.add(new_page)    # 세트에 추가
            get_links(new_page)    # 재귀호출(자기 자신을 호출)

get_links('')
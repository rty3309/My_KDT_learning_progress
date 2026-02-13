# 연관 기사 링크 찾기

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

wiki_url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
urlrequest = Request(wiki_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(urlrequest)

bs = BeautifulSoup(html, 'html.parser')    # bs : 전체 html
body_content = bs.find('div', {'id':'bodyContent'})

pattern='^(/wiki/)((?!:).)*$'
#pattern = '^(/wiki/)'
wiki_links = body_content.find_all('a', href=re.compile(pattern))

for link in wiki_links:
    if 'href' in link.attrs:
        print(link['href'])
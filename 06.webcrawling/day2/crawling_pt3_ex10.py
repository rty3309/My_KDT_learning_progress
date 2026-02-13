# Wikipedia 페이지 가져오기

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

wiki_url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
urlrequest = Request(wiki_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(urlrequest)

bs = BeautifulSoup(html, 'html.parser')
atag_list=bs.find_all('a')
print('<a> 태그 개수: ', len(atag_list))

for link in atag_list:
    if 'href' in link.attrs:
        print(link['href'])
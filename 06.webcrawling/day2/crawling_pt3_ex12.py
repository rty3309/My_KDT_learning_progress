# 링크간 무작위 이동하기

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import random
import re

random.seed(None)
def get_links(article_url):
    wiki_url = 'https://en.wikipedia.org' + article_url
    urlrequest = Request(wiki_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)

    bs = BeautifulSoup(html, 'html.parser')
    bodContent = bs.find('div', {'id':'bodyContent'})
    wiki_url = bodContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    return wiki_url

links = get_links('/wiki/Kevin_Bacon')
print('links 길이: ', len(links))
while len(links) > 0:
    rand_index = random.randint(0, len(links) - 1)
    new_article = links[rand_index].attrs['href']
    print(new_article)
    links=get_links(new_article)
# BeautifulSoup 첫 예제

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

print(bs.h1)
print(bs.span)
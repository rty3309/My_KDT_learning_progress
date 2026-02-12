# 웹 페이지 가져오기

from urllib.request import urlopen

html = urlopen('https://www.daangn.com/hot_articles')
print(type(html))
(print(html.read()))
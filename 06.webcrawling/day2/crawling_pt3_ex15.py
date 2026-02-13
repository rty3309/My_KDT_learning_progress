# 인터넷 크롤링 : URL 구조

from urllib.parse import urlparse

urlString1 = 'https://shopping.naver.com/home/p/index.naver'
# home 부터 path

url = urlparse(urlString1)
print(f'scheme: {url.scheme}')
print(f'netloc: {url.netloc}')
print(f'path: {url.path}')
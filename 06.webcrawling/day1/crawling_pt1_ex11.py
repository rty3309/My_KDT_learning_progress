# User-Agent 사용 비교 : urllib.request, requests

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import requests

def use_urlopen(url):
    # HTTP request 패킷 생성 : Request()
    urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)
    soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
    print(soup)

def use_requests(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(response.encoding)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.text)
    print(soup)

def main():
    melon_url = 'https://www.melon.com/chart/index.htm'
    use_urlopen(melon_url)
    use_requests(melon_url)

main()
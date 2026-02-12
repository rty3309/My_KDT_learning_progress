# 존재하지 않는 태그 예외 처리

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url, tag):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        value = bs.find(tag)
        print(bs.h2.text)
    except HTTPError as e:
        return None
    except AttributeError as e:
        print(f'AttributeError: {e}')
        return None
    else:
        return value

url = 'http://www.pythonscraping.com/pages/page1.html'
tag = 'h2'    # h1 넣으면 정상 출력됨
value = get_title(url, tag)

if value == None:
    print(f'{tag} could not be found')
else:
    print(value)
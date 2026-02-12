# 신뢰할 수 있는 연결과 예외 처리

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')    # page 404
    #html = urlopen('http://www.pythonscraping.com/pages/page1.html')    # it worked
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked')    # 정상인 경우
# 정규 표현식과 BeautifulSoup 1

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

# 정규식: ('img.*.jpg'): img 다음에 임의의 한 문자가 0회 이상
# - img.jpg, img1.jpg, imga.jpg 등
img_tag = re.compile('/img/gifts/img.*.jpg')    # img.*.jpg : img 뒤에 임의의 문자(.)가 *(0 or more)
images = soup.find_all('img', {'src': img_tag})    # img_tag : 패턴 객체

for image in images:
    print(image, end=" -> ['src'] 속성값: ")
    print(image['src'])
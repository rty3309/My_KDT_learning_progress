# 정규 표현식과 BeautifulSoup 2

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs=BeautifulSoup(html, 'html.parser')

prince_list = bs.find_all(string='the prince')
print('the prince count: ', len(prince_list))

prince_list_all = bs.find_all(string=re.compile('[T|t]{1}he prince'))    # | : or 기호
print('T|the prince count:', len(prince_list_all))
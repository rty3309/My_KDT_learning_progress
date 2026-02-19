# urllib.parse.quote('검색어')

from urllib.parse import quote

text  = '파이썬 크롤링'
encoded = quote(text)
print(f'원본: {text}')
print(f'인코딩: {encoded}')

base = 'https://www.google.com/search?q='
query = '파이썬 크롤링'
url = base + quote(query)
print(url)
# 파이썬과 통합 : 위키피디아 자료를 MySQL에 저장

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import random
import pymysql
import re

def store(conn, cur, title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES (%s, %s)',
                 (title, content))
    conn.commit()

def get_links(conn, cur, article_url):
    url = 'http://en.wikipedia.org' + article_url
    urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)

    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').text
    content = bs.find('div', {'id':'mw-content-text'}).find('p').text
    print(title, content)

    # find()로 검색된 데이터를 데이터베이스에 저장
    store(conn, cur, title, content)

    # 해당 url에서 모든 <a> 태그를 리스트에 저장 후 리턴
    bodyContent = bs.find('div', {'id':'bodyContent'})

    wiki_urls = bodyContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))    # url 링크를 저장한 리스트
    return wiki_urls

def main():
    conn = pymysql.connect(host='localhost',  user='jaeheon', password='2580',
                           database='scraping', charset='utf8')
    cur = conn.cursor()

    random.seed(None)
    links = get_links(conn, cur, '/wiki/Kevin_Bacon')
    try:
        while len(links) > 0:
            new_article = links[random.randint(0, len(links)-1)].attrs['href']
            # random.randint(0, len(links)-1) : (1) 무작위로 하나의 링크(url) 선택 후 이동  (2) 새로운 url에서 <a> 태그 저장
            print(new_article)
            links = get_links(conn, cur, new_article)
    except Exception as e:
        print('Exception: ', e)
    finally:
        cur.close()
        conn.close()
        print('MySQL Connection Closed')

main()
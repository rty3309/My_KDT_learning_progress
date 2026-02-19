# 파이썬과 통합

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1111',
                       database='scraping', charset='utf8')

cur=conn.cursor()
cur.execute('use scraping')
cur.execute("SELECT * FROM pages WHERE id=2")

print(cur.fetchone())
cur.close()
conn.close()
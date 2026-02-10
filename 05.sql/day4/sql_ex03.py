# MySQL과 Python 연동하기
# DictCursor 사용 두 가지 방법
# 1) pymysql.connect(…, cursorclass=pymysql.cursors.DictCursor)
# 2) conn.cursor(pymysql.cursors.DictCursor) - 이 방법을 더 추천

import pymysql
import pandas as pd

conn=pymysql.connect(host='localhost', user='root', password='1111',
                     database='sakila', charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)    # 이 부분이 다름(DataFrame의 column 정보도 같이 출력됨)
cur.execute('select * from language')
rows=cur.fetchall()

language_df=pd.DataFrame(rows).set_index('language_id')
print(language_df)
print()

print(language_df['name'])
cur.close()
conn.close()    # 데이터베이스 연결 종료
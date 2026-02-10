# MySQL과 Python 연동하기
# cursor.fetchall() 함수

import pymysql
import pandas as pd

conn=pymysql.connect(host='localhost', user='root',
                     password='1111', database='sakila',
                     charset='utf8')
cur=conn.cursor()
cur.execute('select * from language')
rows=cur.fetchall()    # 모든 쿼리 결과를 가져옴
print(rows)

language_df=pd.DataFrame(rows)
print(language_df)

cur.close()
conn.close()    # 데이터베이스 연결 종료
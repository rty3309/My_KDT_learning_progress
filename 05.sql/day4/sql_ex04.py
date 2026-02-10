# MySQL과 Python 연동하기
# 복잡한 쿼리 실행

import pymysql
import pandas as pd

conn=pymysql.connect(host='localhost', user='root', password='1111',
                     database='sakila', charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)

# 큰 따옴표 사용 : 내부에 문자열('...')을 포함하기 위해
query="""
SELECT c.first_name, c.last_name, c.email
From customer as c
    INNER JOIN rental as r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = %s
"""
# 실제 쿼리와 동일한 문자열만 전달하면 됨(따옴표 주의)
# => 마지막에 세미콜론(;) 없어야 됨

cur.execute(query, '2005-06-14')    # 날짜 : 쿼리에 전달할 값

rows=cur.fetchall()    # 모든 데이터를 가져옴
result_df=pd.DataFrame(rows)    # DataFrame 형태로 변환
print(result_df)
cur.close()
conn.close()
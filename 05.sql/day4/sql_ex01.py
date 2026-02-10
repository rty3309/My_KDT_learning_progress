# PyMySQL의 cursor 정보

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1111',
                       database='sakila', charset='utf8')
# 지금은 local host라서 root(1111), jaeheon(2580) 둘 다 접속 가능한데 
# 다른 컴퓨터랑 연결시에는 root 안됨

cur= conn.cursor()
cur.execute('select * from language')

desc= cur.description    # 헤더 정보를 가져옴
for i in range(len(desc)):
    print(desc[i][0], end=' ')
print()

rows = cur.fetchall()    # 모든 쿼리 결과를 가져옴
for data in rows:
    print(data)
print()

cur.close()
conn.close()    # 데이터벵스 연결 종료
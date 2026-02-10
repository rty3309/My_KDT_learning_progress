# 데이터 추가
# executemany() : 여러 개의 tuple 데이터를 처리

import pymysql

conn=pymysql.connect(host='localhost', user='root', password='1111',
                     database='sqlclass_db', charset='utf8')
curs=conn.cursor()
sql = """INSERT INTO employee(name, office, region)
        VALUES (%s, %s, %s)
        """
data=(
    ('홍진우', 1, '서울'),
    ('강지수', 2, '부산'),    # 튜플 형태로 여러 개의 데이터 전달
    ('김청진', 1, '대구')
)

curs.executemany(sql, data)
# executemany() : 여러 개의 데이터 처리

conn.commit()
print('executemany() 완료')
curs.close()
conn.close()
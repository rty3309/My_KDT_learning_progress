# UPDATE, DELETE

'''
UPDATE, DELETE
'''

import pymysql

conn=pymysql.connect(host='localhost', user='root', password='1111',
                     database='sqlclass_db', charset='utf8')
curs=conn.cursor()
sql = """
    UPDATE employee
    SET region = '서울특별시'
    WHERE region = '서울'
    """
curs.execute(sql)
print('update 완료')

sql="DELETE FROM employee WHERE name=%s"
curs.execute(sql, '홍길동')
print('delete 홍길동')
conn.commit()
curs.close()
conn.close()
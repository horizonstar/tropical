# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = 'admin',
        db = 'test',
        )

cur = conn.cursor()

'''
sqli = "insert into person VALUES(%s,%s)"
#cur.execute(sqli,('12','XiaoMing'))
cur.executemany(sqli,[('14','Liu'),('15','Li'),('16','Sun')])'''


selectsql = cur.execute("select * from person")
print selectsql

info = cur.fetchmany(selectsql)
for ii in info:
    print ii


cur.close()
conn.commit()
conn.close()
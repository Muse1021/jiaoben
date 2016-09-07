#encoding=utf-8
import MySQLdb
conn= MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd='123456',
    charset='utf8',
    db ='school'
)
cur = conn.cursor()
datalist = cur.execute("select * from Teacher")
datas = cur.fetchmany(datalist)
for data in datas:
    print data
cur.close()
conn.commit()
conn.close()
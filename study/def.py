import pymysql
import json

conn = pymysql.connect(host='127.0.0.1', user='zorelu', password='123123zz', db='test', charset='utf8',cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql = "SELECT * FROM user"
cur.execute(sql)
a = cur.fetchall()
print (a)

# u = json.dump(a)
# print(u)
conn.close()
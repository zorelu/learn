import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='tx.zorelu.win',
                             user='root',1
                             password='123123zz',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



cursor = connection.cursor()
        # Read a single record
name=input()
sql = "CREATE USER '{0}'@'localhost' IDENTIFIED BY '123456'".format(name)
cursor.execute(sql)
result = cursor.fetchone()
print(result)

connection.close()
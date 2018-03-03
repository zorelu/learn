import psycopg2
import hashlib

def md5(arg):#这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5(bytes('abd',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()

conn = psycopg2.connect(database="test", user="postgres", password="123123zz", host="web.zorelu.win", port="5432")
print ('Opened database successfully')
cur = conn.cursor()
# ###login code
# user1 = input ("select username :")
# userpwd = input("?? passwd :")
# cur.execute("select passwd  from user1  where username= '{0}'".format(user1))
# rows = cur.fetchall()
# #print  (rows)
# for row in rows:
#     passwd = (str(row[0]))
# if md5(userpwd) == passwd:
#     print ("ok")
# else :
#     print("not ok ")

#### register code



useradd = input ("add username :")
pwdadd = input("add passwd :")
addpwd = md5(pwdadd)
cur.execute("select *  from user1  where username= '{0}'".format(useradd))

rows = cur.fetchall()
cur.close()
print (rows)
####insert code
if  not rows:
     cur = conn.cursor()
     #print(useradd)
     cur.execute("insert into user1 (passwd,username) \
                                         values('{0}','{1}')".format(addpwd,useradd))
     cur.close()
     print('adduser new')

else:
    print("username have")





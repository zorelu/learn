import psycopg2
import hashlib

def md5(arg):#这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5(bytes('abd',encoding='utf-8'))
    md5_pwd.update(bytes(arg,encoding='utf-8'))
    return md5_pwd.hexdigest()

conn = psycopg2.connect(database="test", user="postgres", password="123123zz", host="web.zorelu.win", port="5432")
print ('Opened database successfully')
cur = conn.cursor()




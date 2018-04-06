import psycopg2
import hashlib

conn = psycopg2.connect(database="test", user="postgres", password="123123zz", host="web.zorelu.win", port="5432")
print ('Opened database successfully')
cur = conn.cursor()

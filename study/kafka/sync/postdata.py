###数据库转json到kfka
import psycopg2
import hashlib
from kafka import KafkaProducer
import json


conn = psycopg2.connect(database="test", user="postgres", password="123123zz", host="web.zorelu.win", port="5432")
#print ('Opened database successfully')
cur = conn.cursor()
producer = KafkaProducer(bootstrap_servers='web.zorelu.win:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'),ack=1)


cur.execute("select *  from user1 ")
rows = cur.fetchall()
#print (rows)
for a in rows:
    print (a[0])
    producer.send('test', {'passwd': a[0],'name':a[1]})
conn.close()
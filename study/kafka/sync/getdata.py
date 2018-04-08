from pymssql import connect  # @UnresolvedImport
from kafka import KafkaConsumer
import json
import time
conn = connect(host="gs.zorelu.win", user="sa", password="stsy666",
               database="b2b_bz")
cursor = conn.cursor()

# 消费192.168.120.11:9092上的world 这个Topic,指定consumer group是consumer-20171017
consumer = KafkaConsumer('test', bootstrap_servers=['web.zorelu.win:9092'])
#print(consumer)
for msg in consumer:
    a =  (str(msg.value,encoding="utf8"))
    b = json.loads(a)  # 根据字符串书写格式，将字符串自动转换成 字典类型

    print(b["passwd"])




    cursor.execute("INSERT INTO test1 (id,name)VALUES \
    ('{0}','{1}')".format(b["passwd"],b["name"]))
# you must call commit() to persist your data if you don't set autocommit to True
    conn.commit()

conn.close()
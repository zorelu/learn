#####kafka post  json data
from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='web.zorelu.win:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for _ in range(100):
    producer.send('test', {'foo': 'bar'})
#producer.send('foobar', b'some_message_bytes')

#future = producer.send('test', b'another_message')
#result = future.get(timesdasdout=60)
###kafka get json data
from kafka import KafkaConsumer
import json
import time
# 消费192.168.120.11:9092上的world 这个Topic,指定consumer group是consumer-20171017
consumer = KafkaConsumer('test', bootstrap_servers=['web.zorelu.win:9092'])
#print(consumer)
for msg in consumer:
    a =  (str(msg.value,encoding="utf8"))
    b = json.loads(a)  # 根据字符串书写格式，将字符串自动转换成 字典类型

    print(b["foo"])

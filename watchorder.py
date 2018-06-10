import time
import datetime
from pymongo import MongoClient
import json
import requests
import pymssql

###time
t = time.time()
now = int(round(t * 1000))
print (now)  

###mongdb
moclient = MongoClient()
moclient = MongoClient('mongodb://zorelu:123123zz@tx.zorelu.win:27017/admin')
modb = moclient.b2b
collection=modb.order 
#####mssql
msconn=pymssql.connect(host='tx.zorelu.win',user='sa',password='3877276lzY49',database='test')
cursor = msconn.cursor()


#### run jmster
num = ''
msor= ''
phone = str(13715857400)
#print (phone)
###mongdb gt need 'gt'
result = collection.find({"userName":phone,"creatTime":{'$gt':now}},{"_id":0,"orderNum":1})
if result.count() == 0:
	print ('没有订单数据')
else:
	for data in collection.find({"userName":phone,"creatTime":{'$gt':now}},{"_id":0,"orderNum":1}):
		#print (data.count())
		num = (data['orderNum'])

####
print(num)
cursor.execute('SELECT * FROM test WHERE ordernum=%s', 'num')
rows = cursor.fetchall()
print (rows)
if len(rows):
    for row in rows:
         print (row)

else:
    #print ('not found')
    msor = 'not order num '





msconn.close()
####print report 
###for dingding rebot
		
#print (data['orderNum'])

ddmes ={
           "mongodb订单号" : data['orderNum'],
            "mssql订单号" : "",
            "对应下单的手机号" : phone,
            "测试是否成功" : "",
            "mongdb链接是否正常" :""
        }
import datetime
from pymongo import MongoClient
import json
import requests
#import pymssql

###time
t = time.time()
now = int(round(t * 1000))
print (now)



###mongdb
moclient = MongoClient()
moclient = MongoClient('mongodb://zorelu:123123zz@tx.zorelu.win:27017/admin')
modb = moclient.b2b
collection=modb.order
#####mssql
#conn=pymssql.connect(host='tx.zorelu.win',user='sa',password='3877276lzY49',database='test')

#### run jmster
data = ''
phone = str(13715857400)
#print (phone)
###mongdb gt need 'gt'

###60秒内尝试循环读取数据3次
count = 3
while True:
	#a = a ++
	if count == 0:
		break
	else:
		result = collection.find({"userName":phone,"creatTime":{'$gt':now}},{"_id":0,"orderNum":1})
		if result.count() == 0:
			count -= 1
			print ('没有订单数据')
			time.sleep(60)

		else:
			for data in collection.find({"userName":phone,"creatTime":{'$gt':now}},{"_id":0,"orderNum":1}):
		#print (data.count())
				print (data['orderNum'])
				count -= 1
				time.sleep(60)


####print report
###for dingding rebot

#print (data['orderNum'])

ddmes ={

            "mongodb订单号" : data['orderNum'],
            "mssql订单号" : "",
            "对应下单的手机号" : phone,
            "测试是否成功" : "",
            "mongdb链接是否正常" : "",
            "mssql链接是否正常" : "",
            "预留字段" : ""
        }

user_info = {"msgtype":"text","text":{"content":ddmes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
headers = {'content-type': 'application/json'}
r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=b1ca14093099f4c76ad72424a52f42f5d141d424fe4d96ccc1ed4c424d6fce46", data=json.dumps(user_info), headers=headers)











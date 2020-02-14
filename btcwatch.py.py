from websocket import create_connection
import json
import time
import requests, json
import logging

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    
                    )



while True:  #测试连接
    time.sleep(2)
    try:
        ws = create_connection("wss://www.bitmex.com/realtime?subscribe=trade:XBTUSD", timeout=5)
        # print(ws)
        break
    except Exception as e:
        print('连接异常：', e)
        continue

for i in range(5):#循环5次，先跑掉ws的欢迎词
    # ws.send('{"op": "subscribe", "args": ["trade:XBTUSD"]}')
    response = json.loads(ws.recv())
    print(response)
   

while True:  ###提取关键词
    try:
        response = json.loads(ws.recv())
        # print (type(response))
        # print (response["data"])
        a=response["data"]

        b=a[0]
        datab=int()
      
           
        # print (b["side"])
        print(b["size"])
        logging.debug(b['size'])
        if    500000 <= b["size"] <= 799999:
                nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                headers = {'content-type': 'application/json'}
                mes = "\ud83d\udd35" + "XBTUSD"+ "  " + "时间:" + nowtime +" " + str(b["price"]) + "$" +" "  + str(b["side"]) + " " +" "+ str(b["size"]) 
                user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
                # print("300-500")
                r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=bf3f83ca6ac59e44a2bffb7d8fa5e4204c0b3e9d83be2be515eacc39de6e4423", data=json.dumps(user_info), headers=headers) 
    
        elif  b["size"] > 800000 :
                nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                headers = {'content-type': 'application/json'}
                mes = "\ud83d\udd34"  + "XBTUSD"+  "  " + "时间:" + nowtime +" " + str(b["price"]) + "$" +" "  + str(b["side"]) + " " +" "+ str(b["size"]) 
                user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
                # print("8000")
                r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=bf3f83ca6ac59e44a2bffb7d8fa5e4204c0b3e9d83be2be515eacc39de6e4423", data=json.dumps(user_info), headers=headers)         
           
#报错返回
    except Exception as e:
        # time.sleep(1)
        # nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        # mes =  "测试连接异常："  +  nowtime
        # mes = "获取XBTUSD接口请求超时5秒重新获取"
        # user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
        # headers = {'content-type': 'application/json'}  
        # r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=01f23e1ed8cd2cbb2cc7b909d7b0685ed4983dea79b3c674102b67fe5fb0cd09", data=json.dumps(user_info), headers=headers) 
        continue 

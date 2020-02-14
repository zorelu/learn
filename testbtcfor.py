import requests, json
import time

a=35

if 10 < int(a) <= 20:
    mes ="测试" + "\u26ab\ufe0f"

    user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
    headers = {'content-type': 'application/json'}  
    r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=01f23e1ed8cd2cbb2cc7b909d7b0685ed4983dea79b3c674102b67fe5fb0cd09", data=json.dumps(user_info), headers=headers)  
    time.sleep(2)

elif 20 < int(a) < 50:
    mes ="测试20" + "\u26ab\ufe0f"

    user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
    headers = {'content-type': 'application/json'}  
    r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=01f23e1ed8cd2cbb2cc7b909d7b0685ed4983dea79b3c674102b67fe5fb0cd09", data=json.dumps(user_info), headers=headers)  
    time.sleep(2)


elif  int(a) >50:
    mes ="测试260" + "\u26ab\ufe0f"

    user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
    headers = {'content-type': 'application/json'}  
    r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=01f23e1ed8cd2cbb2cc7b909d7b0685ed4983dea79b3c674102b67fe5fb0cd09", data=json.dumps(user_info), headers=headers)  
    time.sleep(2)

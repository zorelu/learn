###使用钉钉机器人接口进行post数据
###使用bash
#!/bin/bash
###接口地址
url=https://oapi.dingtalk.com/robot/send?access_token=e502a9f5b25cb8061ae0ad89e923b17f7e7c980680db31a2e6cbba8ac64ebe09
b=$(date +%s)
a=$(echo "$b,当前时间")
echo $data
curl -H "Content-type: application/json" -X POST -d '{"msgtype":"text","text":{"content":"'$a'"},"at":{"atMobiles":["15914299850","189xxxx8325"]}}' $url
####输出信息为“当前时间戳加@15914299850”
###使用python
###需要安装requests demjson包
import requests, json
##定义变量
mes ="123"
#print mes
###数据
user_info = {"msgtype":"text","text":{"content":mes},"at":{"atMobiles":["15914299850","189xxxx8325"]}}
headers = {'content-type': 'application/json'}  
r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=e502a9f5b25cb8061ae0ad89e923b17f7e7c980680db31a2e6cbba8ac64ebe09", data=json.dumps(user_info), headers=headers)  
#print r.headers  
#print r.json()  
#print user_info
###输出信息为”123@15914299850“

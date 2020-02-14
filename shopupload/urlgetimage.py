import urllib3
import json
import os

os.chdir(r'e:\code\叮咚商城')
http = urllib3.PoolManager()
imgname="00983495.jpg"
with open(imgname,'rb') as fp:
    #  print(fp)
     file_data = fp.read()
r = http.request(
   'POST',
   'https://s.197.com/web-smp/smp/snsImgUpload',
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
     },    
     fields={
        'filefield': (imgname, file_data),
     }
     )

httpdata=json.loads(r.data.decode('utf-8'))
if httpdata["code"] == "000000":
    imgroute = str(httpdata["data"]).split("|")[0]
#截取前19位后函数
    print(imgroute[19:])
else:
    print("fall")
##use   requests
# import os
# import requests
# os.chdir(r'e:\code\叮咚商城')
# url = 'https://s.197.com/web-smp/smp/snsImgUpload'
# files = {'file': open('00983495.jpg','rb')}
# r = requests.post(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}, files=files,verify=False)
# print(r.text)
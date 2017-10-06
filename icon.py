import os
import requests


##  b为获取当前路径
###  a为输入的网址
b = os.getcwd()
#a= os.path.isdir(b+"/web1")
#print a
if os.path.exists(b+"/web"):
#        print "have file"
else:
#        print "mkdir file"
    os.makedirs(b+"/web")
###判读文件夹是否存在
print "get icon"
a=raw_input("input url:")
url = 'http://{0}/favicon.ico'.format(a)
#print url
#print b
r = requests.get(url) 
with open(b+'/web/'+a+ ".ico", "w+") as code:
         code.write(r.content)
###获取ico图片并写入文件夹

#!/usr/bin/python
import os,sys
import json
import commands


#a = open("/var/named/demo.com",'a')
#a.write("b          IN      A       127.0.0.1")
#a.close( )
#a = raw_input("input:")
#b = os.popen('service named restart')
#print a
#print b
#os.sys()
p = os.popen('curl -I -m 10 -o /dev/null -s -w %{http_code} www.baidu.com')
x = p.read()
print x
 
if "200" in x:
        print "yes"
else:
        print "no"
	print "bind rsetart now"
#	a = open("/var/named/demo.com",'a')
#	a.write("b          IN      A       127.0.0.1")
#	a.close( )
	b = os.popen('service named restart > /dev/null 2>&1 ')


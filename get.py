#!/usr/bin/python
import os,sys
import json
import commands
import psycopg2


###get date and crul status
b = str(504)
name="a.pntryy.com"
os.environ['name']=str(name)
print name
get = os.popen('curl -o /dev/null -s -w "%{http_code}\n " "$name"')
time = os.popen('date +%Y-%m-%d-%H:%M:%S')
time1 = os.popen('date +%s')
date1 = str(time1.read())
date = time.read()
now = get.read()
print   'now is :',now
print    'date is :',date
print    'date1 is :',date1
### sql do
conn = psycopg2.connect(database="test", user="zorelu", password="123123zz", host="127.0.0.1", port="5432")
print "Opened database successfully"
cur = conn.cursor()
##INSERT date and crul status    tables is stats,fields is crul and date, var is now and date ## the %s must use;
cur.execute("INSERT INTO stats (crul,date,date1)VALUES \
(%s,%s,%s)",(now, date,date1))
#INSERT INTO stats (crul,date)VALUES ('%(now)s','%(date)s');
conn.commit()
#cur.execute("select crul from stats where date1 <> (%s);", (date1,))
#slect with where wit var 
cur.execute("select crul from stats where date1 <> (%s) and crul <> (%s);",(date1,b,))
rows = cur.fetchall()
print rows
print len(rows)
print "Records created successfully";
conn.close()


#!/usr/bin/python
import os,sys
import json
import commands
import psycopg2


###get date and crul status

name="a.pntryy.com"
os.environ['name']=str(name)
print name
get = os.popen('curl -I -m 10 -o /dev/null -s -w %{http_code} $name')
time = os.popen('date +%Y-%m-%d-%H:%M:%S')
date = time.read()
now = get.read()
print   'now is :',now
print    'date is :',date
### sql do
conn = psycopg2.connect(database="test", user="zorelu", password="123123zz", host="127.0.0.1", port="5432")
print "Opened database successfully"
cur = conn.cursor()
##INSERT date and crul status    tables is stats,fields is crul and date, var is now and date ## the %s must use;
cur.execute("INSERT INTO stats (crul,date)VALUES \
(%s,%s)",(now, date,))
#INSERT INTO stats (crul,date)VALUES ('%(now)s','%(date)s');
conn.commit()
print "Records created successfully";
conn.close()

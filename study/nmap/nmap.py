import paramiko,psycopg2
from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request


# 创建SSH对象

conn = psycopg2.connect(database="test", user="postgres", password="123123zz", host="web.zorelu.win", port="5432")
print ('Opened database successfully')
cur = conn.cursor()
# 允许连接不在know_hosts文件中的主机
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
cur = conn.cursor()
##都是假的
# cur.execute("select *  from com")
# row = cur.fetchall()
# for parameter in row:
# #    print(parameter[0])


app = Flask(__name__)
@app.route("/login", methods=['post'])
def login():
#parameter='-sS'    request.method == 'POST'
    ip = request.form['nampip']
    ssh.connect(hostname='web.zorelu.win', port=2707, username='root', password='123123zz')


    parameter = request.form['comm']

    com = 'nmap ' + '{0} ''{1}'.format(parameter,ip)
    #print (com)
#执行命令
    stdin, stdout, stderr = ssh.exec_command(com)
# 获取命令结果
    result = str(stdout.read(),encoding="utf8")
    #result=2

    #cur.executemany("insert into nmap (ip,data)values('{0}','{1}')".format(ip, result))
    cur.execute("INSERT INTO nmap (ip,data)VALUES('{0}','{1}')".format(ip, result))
    #cur.execute("INSERT INTO Employee "
     #   "VALUES('Gopher', 'China Beijing', 100, '2017-05-27')")
    conn.commit()
    print(result)
    print(com)
    return 'Post %s' % result
    cur.close()

# 关闭连接

#ssh#cur.close()

app.run(host='0.0.0.0')
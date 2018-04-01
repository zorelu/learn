import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='web.zorelu.win', port=2707, username='root', password='123123zz')
ip='127.0.0.1'
com = 'nmap ' + '{0}'.format(ip)
#print (com)
#执行命令
stdin, stdout, stderr = ssh.exec_command(com)
# 获取命令结果
result = str(stdout.read(),encoding="utf8")

print(result)

# 关闭连接
ssh.close()
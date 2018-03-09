import os,psycopg2

conn = psycopg2.connect(database="test", user="postgres", password="123123zz", host="web.zorelu.win", port="5432")
print ('Opened database successfully')
cur = conn.cursor()
#print os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2]##
##获取当前10个进程并格式或json输出
ml="ps aux | sed -n 5,15p "
###格式第一行
a= os.popen(ml).read().split("\n")
##获取长度


###递归所有,除去第一行（第一行包括其他不需要参数）
##for c  in range(1,len(a)):
#循环10次
for c  in range(10):
	#print (c)
    ###格式第二行
	b=a[c].split()
	print (b)
    # 循环11次
	for d in  range(11):
		print(b[d])


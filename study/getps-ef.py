import os
#print os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2]##
##获取当前10个进程并格式或json输出
ml="ps aux | sed -n 5,15p "
###格式第一行
a= os.popen(ml).read().split("\n")
#循环10次
for c  in range(10):
	#print (c)
    ###格式第二行
	#b=a[c].split()
	print (b)
    # 循环11次
	for d in  range(11):
		print(b[d])


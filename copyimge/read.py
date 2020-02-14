import pypyodbc 
import time
import os 
import shutil
a = os.chdir('D:\\imgestest') 
# print("当前的工作目录为：%s" %os.getcwd())
nowtime = time.strftime('%Y%m%d',time.localtime(time.time()))
liketime = "%" + nowtime + "%"
print (type(liketime))
print(liketime)
db = pypyodbc.win_connect_mdb('D:\\code\MD300L.mdb')
             # 打开数据库连接

# SQL = 'select * from PtBase'
curser = db.cursor()                                    # 产生cursor游标
curser.execute("select ID,Pname  from PtBase where Pbed < '624819' ")
# curser.execute("select  * from PtBase where ID > '2020'  ")
# curser.execute("select ID,Pname from PtBase")
result = curser.fetchall()
for row in result:
    print (row[0])
    print (row[1])
    rename = row[1] + row[0]
    # print (rename)
    #设置各个目录路径
    path1 = ('D:\\code' + '\\' + row[0]) 
    path2 = ('D:\\imgestest') 
    os.mkdir(path2 + './'  + rename )
    path3 = ('D:\\imgestest' + '\\' + rename ) 

    
    # # print(path1)
    for file in os.listdir(path1):
        source_file = os.path.join(path1, file)
        #复制文件
        if os.path.isfile(source_file):
            shutil.copy(source_file, path3) 

   
 

curser.close()


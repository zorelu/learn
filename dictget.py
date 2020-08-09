
x = {'Name': 'Zara', 'Age': "7",'bnnq':"aa","bdc":"asd"}
y = {'Name': 'female' ,'bnnq':"zorelu","bdc":"123"}

d = {}

#判断是否有相同的key有的话输出 
#目前无法需要生成多一个字典
for k,v in x.items():
    # print (k)
    if k in y.keys():
        a = x[k] +","+ y[k]
        temp = dict(zip([k], [a])) 
        d.update(temp) 
# print(d)

#合并xy字典

y.update(x)
y.update(d)
print(y)
##最后把生成的字典与y合并

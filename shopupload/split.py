
httpdata = {
    "code": "000000",
    "data": "http://oss.197.com/201905/15/sns/sns_hnP2iB2Mwy0520JVVJZWT1.jpg|http://oss.197.com/201905/15/sns/sns_hnP2iB2Mwy0520JVVJZWT1.jpg?x-oss-process=image/resize,m_fill,h_200,w_200/quality,q_25",
    "currentTimes": 1558307409893,
    "msg": "操作成功"
}

#截取“|”之前的数据与最后一个"/"后的数据
# imgroute = str(httpdata["data"]).split("|")[0].split("/")[-1]
imgroute = str(httpdata["data"]).split("|")[0]
#截取前19位后函数
print(imgroute[19:])

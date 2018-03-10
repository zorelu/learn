from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
import os

app = Flask(__name__)


# post方法
@app.route("/login", methods=['post'])
def login():
    ##获取当前目录
    #directory = os.getcwd()
    # name = "index.html"
    request.method == 'POST'
    name = request.form['username']
    pw = request.form['passwd']
    ##后缀名
   # name = name1 + ".tar.gz"
    # print(name)

    return '{0}{1}'.format(name,pw)


app.run(host='0.0.0.0')
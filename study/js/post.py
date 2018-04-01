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
    return 'Post %s' % name


app.run(host='0.0.0.0')
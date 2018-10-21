from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import pymysql
import json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 指定使用的数据库的链接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://zorelu:123123zz@127.0.0.1:3306/test"
# 关闭追踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建一个SQLAlchemy对象,需要放在config后面
db = SQLAlchemy(app)


@app.route('/test')

def test(name=None):
    conn = pymysql.connect(host='127.0.0.1', user='zorelu', password='123123zz', db='test', charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql = "SELECT * FROM shop"
    cur.execute(sql)
    u = cur.fetchall()
    # u=json.dump(a)
    print(u['name'])
    # conn.close()
    return render_template('a.html', u=u)
    # return render_template('a.html', name=name)
    # conn.close()
# app.debug = True
app.run(host='127.0.0.1')
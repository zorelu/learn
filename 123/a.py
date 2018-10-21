from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import pymssql
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
@app.route('/test/<name>')
def test(name=None):
    # # todo=(todo.text)
    # conn = pymssql.connect(host="win.zorelu.win", user="sa", password="3877276lzy49", database="test")
    # cursor = conn.cursor()
    # cursor.execute('SELECT  * from [check]')

    # for row in cursor:
    #     # print(row)
    #     name = json.dumps(row,    ensure_ascii=False)
    #     print(name)

    class User(db.Model):
        table_args = {"useexisting": True}
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True)
        email = db.Column(db.String(120), unique=True)

        def __repr__(self):
              return 'nem {0}'.format(self.email)

    u = User.query.all()
    print(u)
    # print(u['id'])

    # for name in a:
    #     a = name.__dict__
    #     print(name)
    return render_template('a.html', u=u)
    # conn.close()
# app.debug = True
app.run(host='127.0.0.1')
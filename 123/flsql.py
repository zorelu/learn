from flask_sqlalchemy import SQLAlchemy
from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import pymssql
import json
app = Flask(__name__)

# 指定使用的数据库的链接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://zorelu:123123zz@127.0.0.1:3306/blog"
# 关闭追踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    table_args = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = emaily

    def __repr__(self):
        return '{},{}'.format(self.username,self.email)

peter = User.query.filter_by(username='admin').all()
a=peter[0]
print(a.email)
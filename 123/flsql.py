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
    __tablename__ = 'users'
    id = db.Column(db.String(100),primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    password = db.Column(db.String(100),nullable=False)

telephone = 15914299850
username = 'zo2relu'
password1 = 'zor2elu'
user = User(username=username,telephone = telephone,password=password1)
db.session.add(user)
db.session.commit()
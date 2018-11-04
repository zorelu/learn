from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    password = db.Column(db.String(100),nullable=False)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    context = db.Column(db.Text,nullable=False)
    # username = db.Column(db.String(100),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now())
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('User',backref='questions')


    # # 隐藏按钮未完成功能
    # hid = db.Column(db.Text, nullable=False)
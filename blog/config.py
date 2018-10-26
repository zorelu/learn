#encoding: utf-8
import os
import pymysql
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'blog'
USERNAME = 'zorelu'
PASSWORD = '123123zz'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = os.urandom(24)
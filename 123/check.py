from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import pymysql
import json
from flask_sqlalchemy import SQLAlchemy

conn = pymysql.connect(host='127.0.0.1', user='zorelu', password='123123zz', db='test', charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql = "SELECT * FROM shop"
cur.execute(sql)
u = cur.fetchall()
\

print(u)




# conn.close()

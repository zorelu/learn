import paramiko,psycopg2
from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'zorelu' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user,
        a = '12312')


@app.route("/login", methods=['post'])
def login():
    request.method == 'POST'
    name = request.form['username']
    return "%s" % name


app.run(host='0.0.0.0')
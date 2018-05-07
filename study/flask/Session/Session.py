from flask import Flask, session, redirect, url_for, escape, request
import os
from datetime import timedelta
app = Flask(__name__)

aa=os.urandom(24)
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        ##session超时设置
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=1)
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = aa
app.debug = True;

app.run(host='0.0.0.0')


###timeout set up
# 构造函数：datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 其中参数都是可选，默认值为0
#
# 下面应该是常识，几乎每个人都知道：
#
#
# 1 millisecond = 1000 microseconds
# 1 minute = 60 seconds
# 1 hour = 3600 seconds
#
# 1 week = 7 days
# from datetime import date, timedelta
#
# print(timedelta.max);  # 999999999 days, 23:59:59.999999
# print(timedelta(days=999999999, hours=23, minutes=59, seconds=59,
#                 microseconds=999999));  # 999999999 days, 23:59:59.999999
#
# print(timedelta.min);  # -999999999 days, 0:00:00
# print(timedelta(-999999999));  # -999999999 days, 0:00:00
#
# print(timedelta.resolution);  # 0:00:00.000001
# print(timedelta(microseconds=1));  # 0:00:00.000001
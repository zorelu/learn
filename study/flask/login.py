from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from sqlcon import md5,cur

app = Flask(__name__)

@app.route('/test')
def test():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'



# post方法
@app.route("/login", methods=['post'])
def login():
    ##获取当前目录
    #directory = os.getcwd()

    # name = "index.html"
    request.method == 'POST'
    name = request.form['username']
    pw = request.form['passwd']
    cur.execute("select *  from user1  where username= '{0}'".format(name))
    rows = cur.fetchall()

    #print (rows)
        # #print(rows)
        # print(md5(pw))
    #for row in rows:
    if not rows:
        return ('please add user')
        # print(useradd)
        # cur.execute("insert into user1 (passwd,username) \
        #                                      values('{0}','{1}')".format(pw,name))

    else:
        for row in rows:
            if pw == row[0]:
               #print(row[0])
                session['username'] = request.form['username']
                #return ('login good')
                return redirect(url_for('test'))
            else:
                #print(rows[0])
                return ('false password')

    cur.close()


@app.route("/register", methods=['post'])
def register():
    ##获取当前目录
    # directory = os.getcwd()

    # name = "index.html"
    request.method == 'POST'
    name = request.form['username']
    pw = request.form['passwd']
    cur.execute("select *  from user1  where username= '{0}'".format(name))
    rows = cur.fetchall()

        # print (row[0])
        # #print(rows)
        # print(md5(pw))
    if not rows:
        cur.execute("insert into user1 (passwd,username) \
                                                values('{0}','{1}')".format(md5(pw), name))
        return ('add user now')
    else:

        return ('please chagne usrname')

    cur.close()

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('test'))
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.run(host='0.0.0.0')
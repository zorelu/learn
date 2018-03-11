from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
from sqlcon import md5,cur

app = Flask(__name__)


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
    for row in rows:

        # print (row[0])
        # #print(rows)
        # print(md5(pw))
        if not rows:
            return ('please add user')
        # print(useradd)
        # cur.execute("insert into user1 (passwd,username) \
        #                                      values('{0}','{1}')".format(pw,name))

        else:
            if md5(pw) == row[0]:
                #print(row[0])
                return ('login good')
            else:
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


app.run(host='0.0.0.0')
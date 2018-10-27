from flask import Flask,render_template,request,redirect,url_for


import config
from exts import db
from models import User


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    # remove the username from the session if it's there

    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    # remove the username from the session if it's there
        if request.method == 'GET':
            return render_template('login.html')
        else:
            pass


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    # remove the username from the session if it's there
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form['telephone']
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']

        user = User.query.filter(User.telephone == telephone).first()
        # print (user)
        if user:
                return '手机号码已经被注册'
        else:
                if password1 != password2:
                    return '密码重复'
                else:
                    user = User(telephone = telephone,username=username,password=password1)
                    db.session.add(user)
                    ###排查排查插入问题
                    # db.session.commit()
                    return redirect(url_for('login'))
app.run(host='127.0.0.1')
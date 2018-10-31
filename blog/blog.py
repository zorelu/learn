from flask import Flask,render_template,request,redirect,url_for,session
from loginreq import login_req
import config
from exts import db
from models import User,Question


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

            telephone = request.form['telephone']
            password = request.form['password']
            user = User.query.filter(User.telephone == telephone,User.password == password).first()
            if user:
                session['user_id'] = user.id
                session.permanet = True
                return redirect(url_for('index'))
            else:
                return '用户名密码错误'

@app.route('/logout/')
def logout():
    # session.clear()
    session.pop('user_id')
    return redirect(url_for('login'))


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

                    ###排查排查插入问题 注册插入数据报错
                    db.session.commit()
                    return redirect(url_for('login'))

@app.route('/question/', methods=['GET', 'POST'])
@login_req
def question():
    # remove the username from the session if it's there
    if request.method == 'GET':
        return render_template('question.html')
    else:
       title  = request.form['title']
       context = request.form['context']
       questions = Question(title=title,context=context)
       user_id = session.get('user_id')
       user = User.query.filter(User.id == user_id).first()
       # print(user)
       question.author = user
       db.session.add(questions)
       db.session.commit()
       return redirect(url_for('index'))

@app.context_processor
def my_context_processoer():
    user_id = session.get('user_id')

    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}

app.run(host='127.0.0.1')
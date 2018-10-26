from flask import Flask,render_template,request


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
        pass


app.run(host='127.0.0.1')
from functools import wraps
from flask import session,redirect,url_for
##登陆限制装饰器,没有登陆无法访问发布问答页面
def login_req(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))

    return  wrapper
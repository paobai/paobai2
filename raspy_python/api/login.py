from flask import Blueprint, render_template, flash, redirect, url_for
import json
from flask import g,request
from models.data import Wendu,Shidu,User
from models.data import *
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user
from flask import current_app

bp = Blueprint("login", __name__)


@bp.route("/html", methods=['GET', 'POST'])
def loginhtml():
    return render_template('login.html')


@bp.route("/register", methods=['GET', 'POST'])
def register_user():
    return render_template('register.html')


@bp.route("/logging/", methods=['GET', 'POST'])
def login_the_user():
    username = request.values.get("username")
    password = request.values.get("password")
    user = User.query.filter_by(username=username).first()
    if user is None:
        #flash('无效的用户名')
        return render_template('login.html')
    if user.password == password:
        print(current_app.login_manager.id_attribute)
        login_user(user)
        #flash('登录成功')
        return redirect(url_for('start'))
    else:
        #flash('无效的密码')
        pass
    return '无效的密码'


@bp.route('/register/', methods=['GET', 'POST'])
def register():
    username = request.values.get("username")
    password = request.values.get("password")

    # 根据表单数据创建用户对象
    user = User(username=username,
             password=password)

    db.session.add(user)

    db.session.commit()

    #flash('注册成功')
    return redirect(url_for('watch.watch_the_state'))


@bp.route('/loginout', methods=['GET', 'POST'])
def loginout():
    logout_user()
    #flash('成功退出！')
    return '成功退出~'
#encoding:gbk
'''
Created on 2014

@author: KEVIN
'''
from flask import render_template,flash,redirect,session, url_for,g
from flask_login import  login_user, logout_user, current_user, login_required
from app import app,oid,lm
from app.forms import LoginForm,EditForm
from app.models import User, ROLE_USER, ROLE_ADMIN
from app.database import db_session
from datetime import datetime
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db_session.add(g.user)  
        db_session.commit()

@app.route('/')
@app.route('/index')

@login_required
def index():
    user = g.user
    return render_template('index.html',
        title = 'Home',
        user = user)
@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', title = 'Sign In',form = form,providers = app.config['OPENID_PROVIDERS'])
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter(User.email == resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname=="":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db_session.add(user)
        db_session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(url_for('index'))

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter(nickname == nickname).first()
    if user == None:
        flash('No such user'+ nickname + '!')
        return redirect(url_for('index'))
    posts =  [
        { 'author': user, 'body': 'Test post #1' },
        { 'author': user, 'body': 'Test post #2' }
    ]
    return  render_template('user.html',user=user,posts=posts)

@app.route('/edit',methods = ['GET','POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db_session.add(g.user)
        db_session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'),404
@app.errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('500.html'),500
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

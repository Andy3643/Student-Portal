from flask import render_template,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm,PitchForm,CommentForm
from models import User
from app import db
from flask_login import login_user,current_user


@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user)
            flash('Thanks for logging in!')
        return redirect(url_for('main.pitch'))
    return render_template('login.html',title = 'login',form = form)
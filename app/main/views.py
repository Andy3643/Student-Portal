from flask import render_template,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm
from app.models import User
from app import db
from flask_login import login_user,current_user

@main.route('/')
def index():
    """
    function to redirect to main page
    """
    return render_template('index.html')
  
# remove to be acceses only on user login
@main.route('/userprofile')
def userprofile():
    
    return render_template('profile.html')



#user registration
@main.route('/sign-up',methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user =  User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save_user()
        

        return redirect(url_for('login'))
    
        title = "New Account"
    return render_template('register.html',signup_form = form)

    
#user login  
@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user)
            flash('Thanks for logging in!')
        return redirect(url_for('main.userprofile'))
    return render_template('login.html',title = 'login',login_form = form)


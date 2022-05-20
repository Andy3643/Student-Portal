
from flask import render_template,request,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm
from app.models import Course, User
from app import db
from flask_login import login_required,current_user, login_user,logout_user
from werkzeug.security import check_password_hash

@main.route('/')
def index():
    """
    function to redirect to main page
    """
    return render_template('index.html')


# @main.route('/login',methods=['GET','POST']) 
# def login():
#     login_form = LoginForm()
#     title = ' user authentication'
#     if login_form.validate_on_submit():
#         user = User.query.filter_by(email = login_form.email.data).first()
#         if user == None:
#             flash('Invalid username or password')
#             return render_template("auth/login.html",login_form = login_form,title = title)
#         the_correct_password = check_password_hash(user.password_hash,login_form.password.data)
#         if the_correct_password == False:
#             flash('Invalid username or password')
#             return render_template("auth/login.html",login_form = login_form,title = title)
#         else:
#             login_user(user,remember=login_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))
    
#     return render_template('register.html',login_form = login_form,title = title)








@main.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            #return check_password_hash(self.password_hash, password)
            #login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Portal login"
    return render_template('profile.html',login_form = login_form,title=title)


# ....
@main.route('/sign-up',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

       #mail_message("Welcome to LinkSpace","email/welcome_user",user.email,user=user)

        return redirect(url_for('main.login'))
        title = "New Account"
    return render_template('register.html',signup_form = form)    


# remove to be acceses only on user login
@main.route('/userprofile')
def userprofile():
    all_course = Course.query.all()
    
    
    
    return render_template('profile.html',courses = all_course)



#post data
@main.route('/insert',methods = ["POST", "GET"])
def insert():
    
    if request.method == 'POST':
        code = request.form['code']
        title = request.form['title']
        
        new_course = Course(code = code, title=title)
        db.session.add(new_course)
        db.session.commit()
    
        
        
        #my_data = Course(code,title)
        #my_data.save_course()
        #db.session.add(my_data)
        #db.session.commit(my_data)
        
        flash ("You have succesfully registered for the course")
        return redirect(url_for('main.userprofile'))
    
#delete course
@main.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Course.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("The course has been deleted")

    return redirect(url_for('userprofile'))








#....
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))





#user registration
# @main.route('/sign-up',methods=['GET','POST'])
# def signup():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user =  User(email = form.email.data, username = form.username.data,password = form.password.data)
#         user.save_user()
        

#         return redirect(url_for('login'))
    
#         title = "New Account"
#     return render_template('register.html',signup_form = form)

    
# #user login  
# @main.route('/login',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email = form.email.data).first()
#         if user != None and user.verify_password(form.password.data):
#             login_user(user)
#             flash('Thanks for logging in!')
#         return redirect(url_for('main.userprofile'))
#     return render_template('login.html',title = 'login',login_form = form)


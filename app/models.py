from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)



    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()    


    @property
    def password(self):
        '''
        prevent user from viewing password
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        '''
        Generates password hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'User {self.username}'


class Course(db.Model):
    __tablename__= 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    code = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self,code,title):
        self.code = code
        self.title = title
        
        
    def save_course(self):
        db.session.add(self)
        db.session.commit()

    def delete_course(self):
        db.session.delete(self)
        db.session.commit()




# @LoginManager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
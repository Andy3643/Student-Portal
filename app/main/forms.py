from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators=[InputRequired()])
    login= SubmitField('Login')
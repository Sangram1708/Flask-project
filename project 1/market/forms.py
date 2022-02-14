from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField


class RegisterForm(FlaskForm):
    username=StringField("Username")
    email=StringField("Email")
    password=PasswordField("password")
    password2=PasswordField("password2")
    submit=SubmitField("Create Account")



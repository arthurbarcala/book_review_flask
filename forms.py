from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField

class SignUpForm(FlaskForm):
    username = StringField('Nome:')
    email = EmailField('Email:')
    password = PasswordField('Password:')
    password2 = PasswordField('Confime a password:')
    submit = SubmitField('Cadastrar')
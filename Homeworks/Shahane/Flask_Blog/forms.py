from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])
    password = PasswordField('Password', validators = [DataRequired()])

    submit = SubmitField('Log in')
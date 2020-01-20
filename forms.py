from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                   EqualTo('password', message='Passwords must be the same.')])
    submit = SubmitField('Register')
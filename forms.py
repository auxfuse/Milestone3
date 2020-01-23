from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password',
                                                                             message='Passwords must be the same.')])
    submit = SubmitField('Register')


class CreateWorkoutForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d')
    focus_name = StringField('Focus')
    location_name = StringField('Location')
    part_a = StringField('Part A')
    part_b = StringField('Part B')
    part_c = StringField('Part C')
    accessory = StringField('Accessory')
    additional_info = StringField('Additional Info')
    coach_notes = StringField('Coach Notes')
    public_session = BooleanField('Public')
    delete = SubmitField('Delete')
    edit = SubmitField('Edit')

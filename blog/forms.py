from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, InputRequired


class LoginForm(FlaskForm):
    username = TextField('Username', validators=[Length(min=4, max=20), InputRequired()])
    password = PasswordField('Password', validators=[Length(min=8, max=80), InputRequired()])
    remember = BooleanField('Remember me', description='Checkboxes can be tricky.')
    submit_button = SubmitField('Submit Form')
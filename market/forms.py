from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(label='Username: ', validators=[Length(min=3, max=40), DataRequired()])
    user_email = StringField(label='Email Address: ', validators=[Email()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password: ', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create Account')
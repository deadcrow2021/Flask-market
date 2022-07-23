from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from .models import User


class AddItemForm(FlaskForm):
    name = StringField(label='Name: ', validators=[Length(min=3, max=40), DataRequired()])
    price = IntegerField(label= 'Price: ', validators=[DataRequired()])
    barcode = IntegerField(label='Barcode: ', validators=[DataRequired()])
    description = TextAreaField(label='Description: ', validators=[Length(max=5000), DataRequired()])
    submit = SubmitField(label='Create Account')



class RegisterForm(FlaskForm):
    username = StringField(label='Username: ', validators=[Length(min=3, max=40), DataRequired()])
    user_email = StringField(label='Email Address: ', validators=[Email()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password: ', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists.')


    def validate_user_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError('Email Address already exists.')



class LoginForm(FlaskForm):
    username = StringField(label='Username: ', validators=[DataRequired()])
    password = PasswordField(label='Password: ', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

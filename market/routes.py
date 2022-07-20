from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, login_required
from .models import Item, User
from .forms import RegisterForm, LoginForm
from . import app, db

@app.route("/")
@login_required
def home_page():
    items = Item.query.all()
    return render_template('home.html', items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.user_email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash('Account has been successfully created.', category='info')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'Error in user creating form: {error_message}', category='danger')
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You was logged in: {attempted_user.username}', category='info')
            return redirect(url_for('home_page'))
        else:
            flash('Username or password are not match. Try again.', category='danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('home_page'))

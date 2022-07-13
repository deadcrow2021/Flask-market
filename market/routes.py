from flask import flash, redirect, render_template, url_for
from .models import Item, User
from .forms import RegisterForm
from . import app, db

@app.route("/")
def home_page():
    items = Item.query.all()
    return render_template('home.html', items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.user_email.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'Error in user creating form: {error_message}', category='danger')
    return render_template('register.html', form=form)

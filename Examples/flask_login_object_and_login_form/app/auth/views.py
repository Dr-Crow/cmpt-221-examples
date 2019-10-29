from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm


# Login view for user
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Get login form
    form = LoginForm()

    # Onces a user submits the form do this
    if form.validate_on_submit():

        # Query the user table by email
        user = User.query.filter_by(email=form.email.data.lower()).first()

        # If user is not empty and password verified
        if user is not None and user.verify_password(form.password.data):
            # Login the user by a built in Flask-Login function. If no remember me value is passed in
            # then when the browser closes the user will be logged out due to session being expired
            login_user(user, form.remember_me.data)

            # Next is set when a user tries to access a page where a login is required. If next is not set, meaning
            # someone tried to directly browse to the login page, we defaultly redirect them to the index page
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)

        # If the email or password incorrect flash a warning
        flash('Invalid email or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

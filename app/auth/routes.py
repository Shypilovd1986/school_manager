from flask import render_template, session, flash, redirect, request, url_for
from . import auth
from .forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('email'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, Вы успешно вошли!", "success")
            login_user(user, form.remember_me.data)
            session['user_id'] = user.id
            session['username'] = user.email
            # User.is_authenticated = True
            return redirect("/index")
        else:
            flash(f"Sorry, something went wrong.{user}", "danger")
    return render_template("auth/login.html", form=form, login=True)


@auth.route("/logout")
def logout():
    logout_user()
    session.pop('username', None)
    # session['user_id'] = False
    # User.is_authenticated = False
    # return redirect(url_for('index'))
    return render_template('auth/logout.html', logout=True)

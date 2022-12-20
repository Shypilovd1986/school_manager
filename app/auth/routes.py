from flask import render_template, session, flash, redirect, url_for
from . import auth
from .forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from app import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('../templates/auth/email'):
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
            flash(f"Логин или пароль не верный!", "danger")
    return render_template("auth/login.html", form=form, login=True)


@auth.route("/logout")
def logout():
    logout_user()
    session.pop('username', None)
    # session['user_id'] = False
    # User.is_authenticated = False
    # return redirect(url_for('index'))
    return render_template('auth/logout.html', logout=True)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('index'))

    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('index'))

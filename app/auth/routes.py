from flask import render_template, session, flash, redirect, url_for
from . import auth
from app.forms import LoginForm
from app.models import User


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
            session['user_id'] = user.id
            session['username'] = user.email
            return redirect("/index")
        else:

            flash(f"Sorry, something went wrong.{user}", "danger")
    return render_template("auth/login.html", form=form, login=True)

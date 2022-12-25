from flask import render_template, session, flash, redirect, url_for, request
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from ..useful_func import send_email


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
    return redirect(url_for('auth.login'))


@auth.route('/confirm')
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Подтвердите свой аккаунт',
               'auth/email/confirm', user=current_user, token=token)
    flash('Новое письмо с подтверждением было отправлено Вам на почту!')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=["POST", "GET"])
def register():
    if session.get('username'):
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
            token = user.generate_confirmation_token()
            send_email(user.email, 'Подтвердите регистрацию!', 'auth/email/confirm', user=user, token=token)
            flash('Вы успешно зарегестрированы!! Подтверждение было отправлено на вашу почту', category='success')
            return redirect(url_for('index'))
        except:
            return 'При регистрации  произошла ошибка'

    return render_template("auth/register.html", form=form, register=True)

@auth.before_app_request
def before_any_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.confirmed or current_user.is_anonymous:
        return redirect(url_for('index'))
    return render_template('auth/unconfirmed.html')

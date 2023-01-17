from flask import render_template, redirect, url_for, flash, session
from flask_login import logout_user, login_required, current_user
from . import personal_cabinet
from .forms import ChangePassword, ResetPassword, NewResetPassword
from .. import db
from werkzeug.security import generate_password_hash
from ..models import User
from ..useful_func import send_email, get_user_id


@personal_cabinet.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePassword()

    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        if not current_user.get_password(current_password):
            flash('Вы ввели неправильный текущий пароль', category='danger')
        elif current_user.get_password(current_password):
            current_user.password = generate_password_hash(new_password)
            try:
                db.session.add(current_user)
                db.session.commit()
                flash('Вы успешно сменили пароль', category='success')
                logout_user()
                session.pop('username')
                return redirect(url_for('auth.login'))
            except:
                return 'При изменение пароля произошла ошибка'
    return render_template('personal_cabinet/change_password.html', change_password=True, personal_cabinet=True, form=form)


@personal_cabinet.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPassword()
    if form.validate_on_submit():
        user_email = form.user_email.data
        user = User.query.filter_by(email=user_email).first()
        if not user:
            flash('Такого пользователя не существует', category='danger')
        else:
            token = user.generate_confirmation_token()
            send_email(user.email, 'Сброс пароля!', 'auth/email/reset_password', user=user, token=token)
            flash('Инструкции для сброса пароля были отправлены Вам на почту', category='success')
            return redirect('/index')
    return render_template('personal_cabinet/reset_password.html', form=form)


@personal_cabinet.route('/new_reset_password/<token>', methods=['GET', 'POST'])
def new_reset_password(token):
    user_id = int(get_user_id(token))
    user = User.query.filter_by(id=user_id).first()
    form = NewResetPassword()
    if form.validate_on_submit():
        new_reset_password = form.new_reset_password.data
        user.password = generate_password_hash(new_reset_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно сменили пароль', category='success')
            logout_user()
            return redirect(url_for('auth.login'))
        except:
            return 'При изменение пароля произошла ошибка'
    return render_template('personal_cabinet/new_reset_password.html', form=form)

@personal_cabinet.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    return render_template('personal_cabinet/change_email.html', change_email=True, personal_cabinet=True)
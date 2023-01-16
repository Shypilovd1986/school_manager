from flask import render_template, redirect, url_for, flash, session
from flask_login import logout_user, login_required, current_user
from . import personal_cabinet
from .forms import ChangePassword, ResetPassword
from .. import db
from werkzeug.security import generate_password_hash
from ..models import User


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
@login_required
def reset_password():
    form = ResetPassword()
    if form.validate_on_submit():
        new_reset_password = form.new_reset_password.data
        confirm_reset_password = form.confirm_reset_password.data
        user_email = form.user_email.data
        user = User.query.filter_by(email=user_email).first()

    return render_template('personal_cabinet/reset_password.html', reset_password=True, personal_cabinet=True, form=form)


@personal_cabinet.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    return render_template('personal_cabinet/reset_password.html', change_email=True, personal_cabinet=True)
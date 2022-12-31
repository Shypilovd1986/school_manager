from flask import render_template, redirect, url_for, flash, session
from flask_login import logout_user, login_required, current_user
from . import personal_cabinet
from .forms import ChangePassword
from .. import db
from werkzeug.security import generate_password_hash


@personal_cabinet.route('/personal_cabinet', methods=['GET', 'POST'])
@login_required
def personal_cabinet():
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
    return render_template('personal_cabinet/personal_cabinet.html', personal_cabinet=True, form=form)

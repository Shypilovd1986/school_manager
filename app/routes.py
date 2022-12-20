from app import app, db, mail
from flask import render_template, flash, session, redirect, url_for
from datetime import datetime
from app.forms import RegistrationForm
from app.models import User
from flask_login import login_required
from app.useful_func import send_email


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html', index=True, current_time=datetime.utcnow())


list_timetable = {'Monday': ['Algebra', 'Chemistry', 'Literature', 'Music'],
                  'thursday': ['Technology ', 'Algebra', 'History', 'Music']
                  }


@app.route('/timetable')
@login_required
def timetable():
    return render_template('timetable.html', list_timetable=list_timetable, timetable=True)


@app.route('/register', methods=["POST", "GET"])
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

    return render_template("register.html", form=form, register=True)
#


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

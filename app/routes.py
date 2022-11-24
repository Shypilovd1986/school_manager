from app import app, db
from flask import render_template, request, flash, session, redirect, url_for
from datetime import datetime
from app.forms import RegistrationForm
from app.models import User


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html', index=True, current_time=datetime.utcnow())


list_timetable = {'Monday': ['Algebra', 'Chemistry', 'Literature', 'Music'],
                  'thursday': ['Technology ', 'Algebra', 'History', 'Music']
                  }


@app.route('/timetable')
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
            flash('Вы успешно зарегестрированы!!', category='success')
            return redirect('/')

        except:
            return 'При регистрации  произошла ошибка'
        # user.set_password(password)

    return render_template("register.html", form=form, register=True)


   # form = LoginForm()
   #  if form.validate_on_submit():
   #      email       = form.email.data
   #      password    = form.password.data
   #
   #      user = User.objects(email=email).first()
   #      if user and user.get_password(password):
   #          flash(f"{user.first_name}, you are successfully logged in!", "success")
   #          session['user_id'] = user.user_id
   #          session['username'] = user.first_name
   #          return redirect("/index")
   #      else:
   #          flash("Sorry, something went wrong.","danger")


@app.route('/logout')
def logout():
    session.pop('username', None)
    # session['user_id'] = False
    return render_template('logout.html', logout=True)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

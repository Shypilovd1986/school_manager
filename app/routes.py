from app import app, db
from flask import render_template, request, flash, session, redirect, url_for
from app.models import User
from datetime import datetime


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html', index=True, current_time=datetime.utcnow())

listTimetable={'Monday': ['Algebra', 'Chemistry', 'Literature', 'Music'],
           'Thusday': ['Technology ', 'Algebra', 'History', 'Music']
               }
@app.route('/timetable')
def timetable():
    return render_template('timetable.html', listTimetable=listTimetable, timetable=True)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        if len(request.form['firstName']) < 3 or len(request.form['lastName']) < 3:
            flash('Слишком короткое имя или фамилия', category='error')
        elif request.form['password'] != request.form['confirmPassword']:
            flash('Подтвержденный пароль и пароль не совпадают!', category='error')
        else:
            user = User(firstName=firstName, lastName=lastName, email=email, password=password)

            try:
                db.session.add(user)
                db.session.commit()
                # flash('Вы успешно зарегестрированы!!', category='success')
                return redirect('/')
            except:
                return 'При регистрации  произошла ошибка'
    return render_template('register.html', register=True)

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        if 'username' in session:
            session['username'] = request.form['email']
            print('method 11111')
            return redirect(url_for('index', username=session['email']))
        elif request.form['email'] == 'shypilovd@gmail.com' and request.form['password'] == '19865421':
            session['userLogged'] = request.form['email']
            return redirect(url_for('index', username=session['userLogged']))
    return render_template('login.html', login=True)

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
def pageNotFound(error):
    return render_template('page404.html'), 404

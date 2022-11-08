from app import app, db
from flask import render_template, request, flash, session, redirect, url_for, abort, current_app
from app.models import User

@app.route('/data')
def get_data():

    return request.environ


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html', index=True)

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
                flash('Регистрация прошла успешно', category='success')
                return redirect('/')
            except:
                return 'При регистрации  произошла ошибка'
    return render_template('register.html', register=True)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if 'userLogged' in session:
            return redirect(url_for('index', username=session['userLogged']))
        elif request.form['email'] == 'shypilovd@gmail.com' and request.form['password'] == '19865421':
            session['userLogged'] = request.form['email']
            return redirect(url_for('index', username=session['userLogged']))
    return render_template('login.html', login=True)

@app.route('/logout')
def logout():
    return render_template('logout.html', logout=True)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404

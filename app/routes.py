from app import app
from flask import render_template, request, flash

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
        if len(request.form['firstName']) < 3 or len(request.form['lastName']) < 3:
            flash('Слишком короткое имя или фамилия', category='error')
        else:
            flash('Регистрация прошла успешно', category='success')
    return render_template('register.html', register=True)

@app.route('/login')
def login():
    return render_template('login.html', login=True)

@app.route('/logout')
def logout():
    return render_template('logout.html', logout=True)


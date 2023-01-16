from app import app, db
from flask import render_template, redirect, url_for, Response, json, jsonify
from flask_login import current_user
from datetime import datetime
from app.models import User
from flask_login import login_required
# from flask_restplus import Resource


# @api.route('/api1', '/api1/')
# class GetAndPost(Resource):
#     def get_data(self):
#         return jsonify(User.query.all())


@app.route('/index', methods=['GET', 'POST'])
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html', index=True, current_time=datetime.utcnow())


list_timetable = {'Monday': ['Algebra', 'Chemistry', 'Literature', 'Music'],
                  'Thursday': ['Technology ', 'Algebra', 'History', 'Music']
                  }


@app.route('/timetable')
@login_required
def timetable():
    if not current_user.confirmed:
        redirect(url_for('auth.unconfirmed'))
    return render_template('timetable.html', list_timetable=list_timetable, timetable=True)


@app.route('/api')
@app.route('/api/<day>')
def show_timetable(day=None):
    if day is None:
        day_timetable = list_timetable
    else:
        day_timetable = list_timetable[day]
    # return Response(json.dumps(day_timetable), mimetype="application/json")
    return jsonify(day_timetable)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

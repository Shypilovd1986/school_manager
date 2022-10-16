from app import app
from flask import render_template

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

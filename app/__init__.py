from flask import Flask
from config import Config
import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_manager.db'
db = SQLAlchemy(app)
db.init_app(app)


# def connect_db():
#     conn = sqlite3.connect(app.config['DATABASE'])
#     conn.row_factory = sqlite3.Row # will show data in form of vocabulary not like tuple
#     return conn    # return connection
#
# def create_db():
#     db = connect_db()
#     with app.open_resource()


from app import routes





from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)


bootstrap = Bootstrap(app)
moment = Moment(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)   # (url_prefix='/auth')

from app import routes

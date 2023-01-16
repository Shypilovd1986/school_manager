from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
# from flask_restplus import Api


app = Flask(__name__)
app.config.from_object(Config)


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app, True)

bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#
# api = Api(app)
# # api.init_app(app)

from .auth import auth as auth_blueprint
from .personal_cabinet import personal_cabinet
app.register_blueprint(auth_blueprint)
app.register_blueprint(personal_cabinet, url_prefix='/personal_cabinet')

from app import routes, errors

import os
from mail_credentials import MAIL_PASSWORD_LOGIN, MAIL_USERNAME_LOGIN

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'6\xe9\xda\xead\x81\xf7\x8d\xbbH\x87\xe8m\xdd3%'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///school_manager.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = MAIL_USERNAME_LOGIN
    MAIL_PASSWORD = MAIL_PASSWORD_LOGIN
    MAIL_SENDER = 'School Manager Admin <shypilovd@gmail.com>'

from flask_mail import Message
from flask import render_template, current_app, flash
from app import mail
from config import Config
from itsdangerous import URLSafeTimedSerializer as Serializer


def send_email(to, subject, template, **kwargs):
    msg = Message(subject, sender=Config.MAIL_SENDER, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


def get_user_id(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)
    except:
        return flash('Во время получения id пользователя из токена произошла ошибка', category='dangerous')
    return user_id.get('confirm')
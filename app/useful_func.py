from flask_mail import Message
from flask import render_template
from app import mail
from config import Config


def send_email(to, subject, template, **kwargs):
    msg = Message(subject, sender=Config.MAIL_SENDER, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

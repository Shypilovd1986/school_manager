from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from flask import current_app
from itsdangerous import URLSafeTimedSerializer as Serializer


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.Text(30), nullable=False)
    password = db.Column(db.Text, nullable=False)
    date_of_registration = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)

    def generate_confirmation_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return f'<User  {self.first_name}  {self.last_name}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

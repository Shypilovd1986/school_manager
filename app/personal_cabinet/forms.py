from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import Length, DataRequired


class ChangePassword(FlaskForm):
    current_password = PasswordField('Старый пароль', validators=[DataRequired(message='Заполните поле!'), Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    new_password = PasswordField('Новый пароль')
    submit = SubmitField('Подтвердить')

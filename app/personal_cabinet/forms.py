from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo


class ChangePassword(FlaskForm):
    current_password = StringField('Старый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                  Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    new_password = StringField('Новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                                 Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов'),
                                                                                 EqualTo('new_password', message='Пароли не совпадают')])
    confirm_new_password = StringField('Подтвердите новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                                 Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов'),
                                                                                 EqualTo('new_password', message='Пароли не совпадают')])
    submit = SubmitField('Подтвердить')

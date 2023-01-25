from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email


class ChangePassword(FlaskForm):
    current_password = StringField('Старый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                  Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    new_password = StringField('Новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                                 Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    confirm_new_password = StringField('Подтвердите новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                                 Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов'),
                                                                                 EqualTo('new_password', message='Пароли не совпадают')])
    submit = SubmitField('Подтвердить')


class ResetPassword(FlaskForm):
    user_email = StringField("Почтовый адрес", validators=[DataRequired(message='Заполните поле!'), Email('Некорректный email')])
    submit = SubmitField('Подтвердить')


class NewResetPassword(FlaskForm):
    new_reset_password = StringField('Новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                 Length(min=8, max=30,
                                                                        message='Пароль должен быть от 8 до 30 символов')])
    confirm_reset_password = StringField('Подтвердите новый пароль',
                                         validators=[DataRequired(message='Заполните поле!'), Length(min=8, max=30,
                                                                                                     message='Пароль должен быть от 8 до 30 символов'),
                                                     EqualTo('new_reset_password', message='Пароли не совпадают')])
    submit = SubmitField('Подтвердить')


class ChangeEmail(FlaskForm):
    current_email = StringField('Текущая почта', validators=[DataRequired(message='Заполните поле!'), Email('Некорректный email')])
    new_email = StringField('Новая почта', validators=[DataRequired(message='Заполните поле!'), Email('Некорректный email')])
    confirm_new_email = StringField('Введите повторно новую почту', validators=[DataRequired(message='Заполните поле!'), Email('Некорректный email'),
                                                                 EqualTo('new_email', message='Почты не совпадает')])
    submit = SubmitField('Подтвердить')


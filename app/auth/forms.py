from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("Почтовый адрес", validators=[DataRequired(message='Заполните поле!'), Email('Некорректный email')])
    password = PasswordField("Пароль", validators=[DataRequired(message='Заполните поле!'), Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")

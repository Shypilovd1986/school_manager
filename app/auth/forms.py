from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    email = StringField("Почтовый адрес", validators=[DataRequired(message='Заполните поле!'), Email('Некорректный email')])
    password = PasswordField("Пароль", validators=[DataRequired(message='Заполните поле!'), Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class RegistrationForm(FlaskForm):
    first_name = StringField("Имя", validators=[DataRequired(), Length(min=2, max=10, message='Имя должно быть больше 2'
                                                                                              ' и меньше 10 символов')])
    last_name = StringField("Фамилия", validators=[DataRequired(), Length(min=2, max=20, message='Фамилия должно быть'
                                                                                    ' больше 2 и меньше 10 символов')])
    email = StringField("Почтовый адрес", validators=[DataRequired(), Length(min=2, max=30, message='Почта должна быть'
                                                                ' не больше 30 символов'), Email('Некорректный email')])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=8, max=30, message='Пароль должен быть '
                                                                                               'от 8 до 30 символов')])
    confirmPassword = PasswordField("Подтверждение пароля", validators=[DataRequired(), EqualTo("password",
                                                                                    message='Пароли не совпадают')])
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Почтовый адрес занят, выберите другой")


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError
from ..models import User

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
    new_reset_password = StringField('Новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                                 Length(min=8, max=30, message='Пароль должен быть от 8 до 30 символов')])
    confirm_reset_password = StringField('Подтвердите новый пароль', validators=[DataRequired(message='Заполните поле!'),
                                                                               Length(min=8, max=30,
                                                                                      message='Пароль должен быть от 8 до 30 символов'),
                                                                               EqualTo('new_reset_password', message='Пароли не совпадают')])
    submit = SubmitField('Подтвердить')

    def validate_email(self, user_email):
        user = User.query.filter_by(email=user_email.data).first()
        if not user:
            raise ValidationError("Введенный почтовый адрес не зарегистрирован, выберите другой")
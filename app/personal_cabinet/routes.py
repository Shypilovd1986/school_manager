from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from . import personal_cabinet


@personal_cabinet.route('/personal_cabinet')
@login_required
def personal_cabinet():
    return render_template('personal_cabinet/personal_cabinet.html', personal_cabinet=True)


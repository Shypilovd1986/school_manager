from flask import Blueprint

personal_cabinet = Blueprint('personal_cabinet', __name__)

from . import routes

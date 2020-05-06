from flask import Blueprint
from flask_login import login_required

blueprint = Blueprint('editorial', __name__)

@blueprint.route('')
@login_required
def board():
    return "dashboard"
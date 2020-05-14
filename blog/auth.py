from .models import User
from .forms import LoginForm
from .utilities import login_manager
from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, redirect, url_for

blueprint = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user=user, remember=form.remember.data)
            return redirect(url_for('editorial.board'))

    return render_template('login.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog'))

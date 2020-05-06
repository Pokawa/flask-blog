from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_nav.elements import Navbar, View 
from flask_nav import Nav

database = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'login'

nav = Nav()
topbar = Navbar('Flask-Blog',
    View('Latest', 'blog.home'),
    View('Most popular', 'blog.home'))
nav.register_element('top', topbar)

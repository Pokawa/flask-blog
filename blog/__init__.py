from flask import Flask
from .utilities import database, login_manager, nav
from .blog import blueprint as blog_blueprint
from .auth import blueprint as auth_blueprint
from .editorial import blueprint as editorial_blueprint
from flask_bootstrap import Bootstrap


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config, silent=True)

    database.init_app(app)
    login_manager.init_app(app)
    nav.init_app(app)

    Bootstrap(app)

    app.register_blueprint(blog_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(editorial_blueprint, url_prefix='/editorial')

    return app

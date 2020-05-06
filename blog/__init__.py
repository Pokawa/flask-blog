from flask import Flask
from .utilities import db
from .blog import blueprint as blog_blueprint


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config, silent=True)
    db.init_app(app)

    app.register_blueprint(blog_blueprint)

    return app
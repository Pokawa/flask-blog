from flask import Flask
from .ext import db
from .blog import blueprint


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config, silent=True)
    db.init_app(app)

    app.register_blueprint(blog.blueprint)

    return app
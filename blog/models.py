from .utilities import database
from flask_login import UserMixin


class Article(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    lead = database.Column(database.String(500))
    text = database.Column(database.Text)
    time_posted = database.Column(database.DateTime)
    visible = database.Column(database.Boolean)


class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), nullable=False)
    password = database.Column(database.String(80), nullable=False)
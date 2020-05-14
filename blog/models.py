from .utilities import database
from flask_login import UserMixin


tags = database.Table('tags',
                      database.Column('article_id', database.Integer, database.ForeignKey('article.id')),
                      database.Column('tag_id', database.Integer, database.ForeignKey('tag.id')))


class Article(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    lead = database.Column(database.String(500))
    text = database.Column(database.Text)
    time_posted = database.Column(database.DateTime)
    visible = database.Column(database.Boolean)
    author_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    tags = database.relationship('Tag', secondary=tags, lazy='subquery', backref=database.backref('pages', lazy=True))


class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), nullable=False)
    password = database.Column(database.String(80), nullable=False)
    displayname = database.Column(database.String(80), nullable=False)
    bio = database.column(database.Text)
    articles = database.relationship('Article', backref='author')


class Tag(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80), nullable=False)

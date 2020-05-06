from .utilities import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    lead = db.Column(db.String(500))
    text = db.Column(db.Text)
    time_posted = db.Column(db.DateTime)
    visible = db.Column(db.Boolean)
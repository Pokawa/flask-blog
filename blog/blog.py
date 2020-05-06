from flask import Blueprint, render_template
from .models import Article

blueprint = Blueprint('blog', __name__)

@blueprint.route('/')
def home():
    query = Article.query.filter_by(visible=1).order_by(Article.time_posted.desc()).all()
    return render_template('articles.html', articles=query)

@blueprint.route('/article/<int:id>')
def article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

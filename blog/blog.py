from flask import Blueprint, render_template
from .models import Article

blueprint = Blueprint('blog', __name__)

@blueprint.route('/')
def home():
    return "Home page"

@blueprint.route('/article/<int:id>')
def article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

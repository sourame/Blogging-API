# core/views page
from flask import render_template, request, Blueprint
from BlogApp.blog_posts.views import blog_post
from BlogApp.models import BlogPost

core = Blueprint('core',__name__)

#HOME page view
@core.route('/')
def index():
    # Querying a limited number of posts and then call paginate 
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page = page, per_page = 10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')

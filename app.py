from distutils.log import debug
from flask_restful import Api
from code import app
from code.resources.blogPost import BlogPost, BlogPostList
from code.resources.user import UserRegister


#*********************
#   API SETUP
#*********************
api = Api(app)

api.add_resource(UserRegister,'/user')
api.add_resource(BlogPost,'/blog/<int:user_id>')
api.add_resource(BlogPostList,'/blogs')

if __name__ == '__main__':
    app.run()

from turtle import title
from flask_restful import Resource, reqparse
from code.models import BlogPostModel

class BlogPost(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("title", type = str, help = "Title can't be blank.") 
    parser.add_argument("text", type = str, help = "Text can't be blank.")
    #parser.add_argument("User Id", type = str, help = "User Id can't be blank.")

    def get(self, user_id):
        bpost = BlogPostModel.find_by_user(user_id)
        if bpost:
            return bpost.json()
        return {'message': 'No posts found'}, 404

    def post(self,user_id):        
        data = BlogPost.parser.parse_args()               
        bpost = BlogPostModel(user_id,data['title'],data['text'])
        try:
            bpost.save_to_db()
        except:
            return {"message": "An error occurred inserting the post."}, 500
        
        return bpost.json(), 201
    
    def delete(self,user_id):
        data = BlogPost.parser.parse_args()        
        bpost = BlogPostModel.find_by_title(user_id,data['title'])
        print(bpost)
        if bpost:
            bpost.delete_from_db()
            return {'Message': 'Blog Post deleted successfully'}
        return {'Message': 'Blog Post not found'}, 404

    def put(self,user_id):
# update operation needs both old and new titles to get the particular post and change it.
        data = BlogPost.parser.parse_args()
        bpost = BlogPostModel.find_by_title(user_id,data['title'])          
        print('Title = ',data['title'])
        print('Text = ',data['text'])
        if bpost:
            bpost.title = data['title']
            bpost.text = data['text']
        else:
            bpost = BlogPostModel(user_id,data['title'],data['text'])

        print('Bpost title = ',bpost.title)
        print('Bpost text = ',bpost.text)
        print('User id = ',bpost.user_id)

        try:
            bpost.save_to_db()
        except:
            return {"message": "An error occurred while updating the post."}, 500
        
        return bpost.json(), 201


class BlogPostList(Resource):
    def get(self):
        return {'All Posts':list(map(lambda x: x.json(),BlogPostModel.query.all()))}


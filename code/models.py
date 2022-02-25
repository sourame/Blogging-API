from code import db
from email.policy import default
from turtle import back
from itsdangerous import json

from sqlalchemy import PrimaryKeyConstraint
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    #posts = db.relationship('BlogPostModel',lazy = 'dynamic')
    posts = db.relationship("BlogPostModel",back_populates = "users", lazy = 'dynamic')

    def __init__(self, email,username, password):
        self.email = email
        self.username = username
        self.password = password

    def json(self):
        return {'Email': self.email, 'Username': self.username, 'Password':self.password,
                'User Id': self.id,'Posts': [post.json() for post in self.posts.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first()

class BlogPostModel(db.Model):
    
    __tablename__ = 'blogposts'    

    id = db.Column(db.Integer,primary_key = True)    
    title = db.Column(db.String(140),nullable = False)
    date = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    text = db.Column(db.Text,nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    #users = db.relationship('UserModel')
    users = db.relationship("UserModel", back_populates = "posts")

    #def __init__(self,title,text,user_id) :
    def __init__(self,user_id,title,text) :
        self.title = title
        self.text = text
        self.user_id = user_id        
    
    def json(self):
        post_date = json.dumps(self.date,default = str)
        print(post_date)
        return {'id':self.id,'Title': self.title, 'Author': self.user_id , 
                'Date': post_date,'Text': self.text}

    @classmethod
    def find_by_user(cls,user_id): 
        return cls.query.filter_by(user_id = user_id).first()
    
    @classmethod
    def find_by_id(cls,user_id,id):        
        return cls.query.filter_by(user_id = user_id, id=id).first()

    @classmethod
    def find_by_title(cls,user_id,title):        
        return cls.query.filter_by(user_id = user_id, title = title).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
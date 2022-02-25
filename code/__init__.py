import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt import JWT

#from security import authenticate, identity
#from resources.user import UserRegister


app = Flask(__name__)


#*********************
#   DATABASE SETUP
#*********************
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'my_secret_key'

db = SQLAlchemy(app)
Migrate(app,db)

#jwt = JWT(app,authenticate,identity)
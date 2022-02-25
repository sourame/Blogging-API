from flask_restful import Resource, reqparse

from code.models import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email",type = str, help = "Email can't be blank.")
    parser.add_argument("username",type = str, help = "Username can't be blank.")
    parser.add_argument("password", type = str, help = "password can't be blank.")

    def get(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return user.json()
        return {'message': 'No User found'}, 404

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"Message":"A user with that name already exists."}, 400

        user = UserModel(data['email'],data['username'], data['password'])
        user.save_to_db()
        user.json()
        return {"Message":"User created successfully."}, 201

        
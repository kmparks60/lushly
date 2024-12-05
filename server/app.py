from config import app, db, api, bcrypt
from flask import Flask, request, make_response, jsonify
from bson import ObjectId
from flask_restful import Resource
# from datetime import datetime

# @app.route('/')
# def index():
#     return 'Hello World!'


# @app.route('/add_user', methods=['POST'])
# def add_user():
#     user_data = request.get_json()

#     name = user_data.get('name')
#     email = user_data.get('email')


#     users_collection = db.users
#     user = {
#             '_id': str(ObjectId()),
#             'name': name,
#             'email': email
#         }

#     result = users_collection.insert_one(user)
#     return f'User added successfully. User ID: {result.inserted_id}'

# --------------------------------------------------------------------------- #
# ----------------------------------- RESTFUL ------------------------------- #

class HomePage(Resource):
    def get(self):
        return {'message':'Hello World'}, 200

class Users(Resource):
    def get(self):
        users_collection = [u for u in db.users.find()]
        return make_response(users_collection, 200)

    def post(self):
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')

        users_collection = db.users
        user = {
                '_id': str(ObjectId()),
                'name': name,
                'email': email
            }

        result = users_collection.insert_one(user)
        return make_response(f'User added successfully. User ID: {result.inserted_id}', 201)

class UserByID(Resource):
    def get(self, user_id):
        user = db.users.find_one({"_id": user_id})
        if user:
            return make_response(user, 200)
        else:
            return make_response({'message': 'User not Found, please try again'}, 404)

    def patch(self, user_id):
        user = db.users.find_one({"_id": user_id})
        if user:
            updated_data = request.get_json()

            for key in updated_data.keys():
                user[key] = updated_data[key]

            db.users.update_one({"_id": user_id}, {"$set": user})
            return make_response(f'Info of User with ID: {ObjectId(user_id)} has been changed!', 201)
        else:
            return make_response({'message': 'User not Found, please try again'}, 404)

    def delete(self, user_id):
        user = db.users.find_one({"_id": user_id})
        if user:
            db.users.delete_one(user)
            return make_response(f'User with ID: {ObjectId(user_id)} has been deleted!', 204)
        else:
            return make_response({'message': 'User either not Found or was deleted, please try again'}, 404)




# ----------------------------------- ROUTES ------------------------------- #
api.add_resource(HomePage, '/')
api.add_resource(Users, '/users')
api.add_resource(UserByID, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
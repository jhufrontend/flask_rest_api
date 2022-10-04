"""
Author: Tony Lee
Description: Class for users of the API, includes admins, registered users, or [guests,]
"""

from flask import request, jsonify
from flask_restful import Resource

from .database import UserDAO

userDao = UserDAO()

class Users(Resource):
    '''CRUD methods for user objects in the database'''
    def post(self):
        '''Method route for adding a user to the database for the API'''
        data = request.json
        username = data['username']
        password = data['password']

        if username is None or password is None:
            return "Missing Arguments", 400 # missing arguments
        if userDao.get_user(username) is not None:
            return "User already exists", 400 # existing user

        if not userDao.add_user(username, password):
            return jsonify({"error": "could not add user"})

        return "success", 200

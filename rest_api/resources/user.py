"""
Author: Tony Lee
Description: Class for users of the API, includes admins, registered users, or [guests,]
"""

from flask import request, jsonify, g
from flask_restful import Resource, Api

from .database import UserDAO

from . import auth

userDao = UserDAO()

class Users(Resource):
    def post(self):
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

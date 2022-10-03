"""
Author: Tony Lee
Description: Class for users of the API, includes admins, registered users, or [guests,]
"""

from flask import request, jsonify, g
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api

from .database import UserDAO

auth = HTTPBasicAuth()

userDao = UserDAO()

class User(Resource):

    @auth.login_required
    def post(self):
        data = request.json
        username = data['username']
        password = data['password']

        if username is None or password is None:
            return "Missing Arguments", 400 # missing arguments
        if User.query.filter_by(username = username).first() is not None:
            return "User already exists", 400 # existing user

        if not userDao.add_user(username, password):
            return jsonify({"error": "could not add user"})
        
        return "success", 200

    @auth.verify_password
    def verify_password(username, password):
        user = User.query.filter_by(username = username).first()
        if not user or not user.verify_password(password):
            return False
        g.user = user
        return True
        

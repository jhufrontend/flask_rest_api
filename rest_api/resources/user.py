"""
Author: Tony Lee
Description: Class for users of the API, includes admins, registered users, or [guests,]
"""

from flask_restful import Resource, Api

class User(Resource):
    def post(self):

        return "Success", 200

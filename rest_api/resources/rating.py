"""
Author: Tony Lee
Description: Everything related to the rating resource grouped here.
"""
from flask import request
from flask_restful import Resource

class RateMovie(Resource):
    def post(self):
        data = request.json
        user_id = data['user_id']
        movie_id = data['movie_id']

        return "Success", 200

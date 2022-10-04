"""
Author: Tony Lee
Description: Everything related to the rating resource grouped here.
"""
from flask import jsonify, request
from flask_restful import Resource

from . import auth
from .database import RatingDAO

ratingDao = RatingDAO()

class RateMovie(Resource):
    '''CRUD methods for rating objects in the database'''
    @auth.login_required
    def post(self, id):
        data = request.json
        username = auth.current_user()

        value = data['value']

        if not ratingDao.add_rating(id, username, value):
            return jsonify({"error": "could not rate movie"})

        return "Success", 200

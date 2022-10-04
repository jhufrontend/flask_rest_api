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
    def post(self, movie_id):
        '''Route to add a rating for a movie in the database'''
        data = request.json
        username = auth.current_user()

        value = data['value']

        if not ratingDao.add_rating(movie_id, username, value):
            return jsonify({"error": "could not rate movie"})

        return "Success", 200

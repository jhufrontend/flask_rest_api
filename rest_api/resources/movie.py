"""
Author: Tony Lee
Description: Everything related to the movie resource grouped here.
"""
from flask import request, jsonify
from flask_restful import Resource

class Movies(Resource):
    def get(self):
        movies = None # db.query.all("movies")
        return jsonify(movies)


class AddMovie(Resource):
    def post(self):
        data = request.json
        movie = {"title": data['title']}

        return jsonify(movie)


class EditMovie(Resource):
    def put(self):
        data = request.json
        movie_id = data['movie_id'] # "to be deleted" # db.session.remove(movie, pk)

        return "Updated", 200


class RemoveMovie(Resource):
    def delete(self, pk):
        data = request.json
        movie_id = data['movie_id'] # "to be deleted" # db.session.remove(movie, pk)

        return "Deleted", 200

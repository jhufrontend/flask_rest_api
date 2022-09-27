"""
Author: Tony Lee
Description: Models and ORM for the API datastore.
"""
from .resources.database import db

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    rating = db.Column() # foreign key to rating model

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    movies = db.Column()  # list of movie ids

class Rating(db.Model):
    __tablename__ = "rating"
    id = db.Column() # composite of user and movie
    value = db.Column(db.Integer, nullable=False)

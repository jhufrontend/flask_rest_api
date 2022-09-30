"""
Author: Tony Lee
Descriptin: Database initialization, setup, and helper procedures.
"""
from datetime import datetime
import sqlalchemy

from models import db
from models import Movie, User, Rating


class UserDAO:
    '''
    CRUD methods for user objects in the database
    '''
    def __init__(self):
        pass

    def create_user(self, username):
        '''Add a new user to the database'''
        user = User(username)

        try:
            db.session.add(user)
            db.session.commit()
        except:
            return False
        
        return True


class MovieDAO:
    '''
    CRUD methods for movie objects in the database
    '''
    def add_movie(self, title, released):
        '''Add new movie to the database'''
        movie = Movie(title=title, released=released)

        try:
            db.session.add(movie)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return False
        
        return True

    def get_movies(self, id=None, user_id=None):
        '''Read movies from the database based on certain filters'''
        result = None
        try:
            if id != None:
                result = db.session.query(Movie).get(id)
            elif id == None and user_id == None:
                result = db.session.query(Movie).all()
            else:
                # result = db.query(Movie).filter(Movie.rating_id==user_id)
                pass
        except Exception as e:
            print(e)

        return result

    def update_movie(self, id, title, released):
        '''Update a movie record in the database'''
        try:
            db.session.query(Movie).filter(Movie.id == id).update({
                Movie.title: title,
                Movie.released: released
            })
            db.session.commit()
        except AttributeError:
            db.session.rollback()
            return False

        return True

    def delete_movie(self, id):
        '''Remove a movie from the database'''
        try:
            db.session.query(Movie).filter(Movie.id == id).delete()
            db.session.commit()
        except AttributeError:
            db.session.rollback()
            return False
        
        return True

class RatingDAO:
    pass


class DbSetup():
    '''
    Initialize and set up the database, by creating tables as necessary
    and inserting dummy records as a starting point.
    '''
    movies = [
        {"title": "Avengers: Endgame", 
        "released": datetime.strptime("04-22-2019", "%m-%d-%Y")},
        {"title": "Captain America: Civil War",
        "released": datetime.strptime("04-16-2016", "%m-%d-%Y")}
    ]
    def __init__(self):
        '''constructor will create all tables for the database.'''
        db.create_all()
        self.prepopulate()

    def prepopulate(self):
        '''Add records to the database after intial creation of tables.'''
        # insert into user

        # insert into movie
        movieDao = MovieDAO()
        for movie in self.movies:
            movieDao.add_movie(movie['title'], movie['released'])

        # insert into rating
        pass


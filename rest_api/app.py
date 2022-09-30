"""
Author: Tony Lee
Description: Man driver program.
"""

from flask import Flask
from flask_restful import Resource, Api

from resources.user import User
from resources.movie import Movies, AddMovie, EditMovie, RemoveMovie
from resources.rating import RateMovie
from resources.database import db, DbSetup

### Allowed routes
routes = '''<ol>
<li> /movies (GET => retrieve all movies) </li>
<li> /add_user (POST - add API users - everyone can signup to use API) </li>
<li> /add_movie (POST => action by admins only - authentication/authorization) </li>
<li> /edit_movie/id (PUT => action by admins only - authentication/authorization) </li>
<li> /delete_movie/id (POST => action by admins only - authentication/authorization) </li>
<li> /rate_movie/id (POST => add a rating to a movie - include guest users) </li>
</ol>'''

app = Flask(__name__)
api = Api()


app.config["SECRET_KEY"] = "iC&diiDF^6754rSycvYDFXydhg08uvh"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =  True


class Intro(Resource):
    def get(self):
        return '<h1>Allowed Routes</h1>' + routes.replace("\n", "")


api.add_resource(Intro, "/")
api.add_resource(User, "/add_user")
api.add_resource(Movies, "/movies")
api.add_resource(AddMovie, "/add_movie")
api.add_resource(EditMovie, "/update_movie/<int:pk>")
api.add_resource(RemoveMovie, "/delete_movie/<int:pk>")
api.add_resource(RateMovie, "/rate_movie/<int:id>")

@app.before_first_request
def app_database_setup():
    DbSetup()

if __name__ == "__main__":
    
    # initialize the database with the app context
    db.init_app(app)
    
    # initialize the api witht the app context
    api.init_app(app)

    # run the server
    app.run(host='0.0.0.0', debug=True)

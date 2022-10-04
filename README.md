# flask_rest_api
sample rest API using flask/flask-restful

# Introduction
The project is a movie rator API. Users can give rating scores to movies and view the movies with their ratings. The backend storage for the API is sqlite3 database that gets setup during the initial deployment of the application. The database consists of users, movies, and ratings.
## Goals
The primary goal of the project is to expose a movie rating database to end users. Users can signup to use the rating services for movies stored in the database. Registered users can add movies to the database, edit the movies or even delete particular movies. Such users can also give ratings to the movies in the database. The API also allows users to view movies with their ratings without having to explicitly sign up to use it.
## Design
The application uses object oriented programming paradigm to achieve an abstract design of the core functionalities of the API. In particular, it uses the flask-restful module to create API resources and expose them to various endpoints as desired. Similarly, the database module used is SQLAlchemy which provides object relational mappings between python objects and database objects. With this ORM, it is possible to change the database technology in the future, say to a more robust MYSQL, without vast modification of the code. Database operations such as insertion, deletion, updates, and reads are also hidden behind classes and methods that can be shared across the applicaition. At the moment, the application runs on the flask server that comes bundled with flask but can be deployed to other production servers.
## Limitations
This is a small application with entry level functionalities which makes it open to certain limitations and development level flaws. Some of these flaws include.
- All registered users can add, update, and delete movies,
- A user can rate a movie more than once
- Loosely coupled database entity relationships,
- Movie ratings calculated each time when a request to get movies is made,
- Loose handling of exceptions with sometimes generalized excaptions caught,
- Generic error messages thrown for different exceptions,

Some of the above limitations can be mitigated by additional development, whereas others can be solved by the frontend application that leverages the API. There is
sufficient room for improving the application and given more time, I could do better. For instance, I could check if the user has already rated a particular movie
and avoid repetitive rating by throwing an error. I would also have admin users who can manipulate the movie objects in the database and regular users who could
only rate movies.

One of the requirements for the project was to achieve a perfect score in pylint tests. While I tried my best to follow the best coding practices, some generic code
styles could not pass pylint tests. One of them was the SQLAlchemy db object. Pylint could not recognize that it had attribute Column and the varied key word
arguments that could appear in such objects. However, some files were able to individually attain perfect scores in pylint when not combined as an entire project.

## Usage
To run the application, certain requirements must be fullfilled. To begin with, the system must have python installed. From here, the system could create a virtual environment and install the modules listed in requirements.txt files using the following commands.
 ```shell
python -m venv venv
pip install -r requirements.txt
```
After successful installation of requirements, proceed to deploy the application via the command below.
```shell
python rest_api/app.py
```
All the commands are relative to the directory containing the main project files.
With the server up, there are multiple ways to test the endpoints. Using the client of choice, in my testing I used postman, one can visit the various endpoints and view the results of the API calls. The generic paths to view endpoints supported by the API are: 
```shell
http://localhost:5000/
http://127.0.0.1:5000/
```
The above paths assume the app was deployed locally and the port was never changed from the defualt 5000 provided by Flask.

## Demo
Attached video. 

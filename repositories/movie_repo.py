from models.movie import Movie
from database.db import db

def save_movie(movie):
    db.session.add(movie)
    db.session.commit()

def get_all_movies():
    return Movie.query.all()

def search_movie(name):
    return Movie.query.filter(Movie.title.ilike(f"%{name}%")).all()

def get_movies_by_provider(provider_id):
    return Movie.query.filter_by(provider_id=provider_id).all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)
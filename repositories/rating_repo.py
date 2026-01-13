from models.rating import Rating
from database.db import db

def save_rating(rating):
    db.session.add(rating)
    db.session.commit()

def get_ratings_by_movie_id(movie_id):
    return Rating.query.filter_by(movie_id=movie_id).all()
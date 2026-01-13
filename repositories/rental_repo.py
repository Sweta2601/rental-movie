from models.rental import Rental
from database.db import db

def save_rental(rental):
    db.session.add(rental)
    db.session.commit()
    return rental

def get_rental_by_id(rental_id):
    return Rental.query.get(rental_id)

def update_rental():
    db.session.commit()


def get_all_rentals():
    return Rental.query.all()

def get_rental_by_id(rental_id):
    return Rental.query.get(rental_id)

def get_rentals_by_user(user_id):
    return Rental.query.filter_by(user_id=user_id).all()

def get_rentals_by_movie(movie_id):
    return Rental.query.filter_by(movie_id=movie_id).all()

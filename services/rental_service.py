from datetime import date
from models.rental import Rental
from repositories.rental_repo import (
    save_rental, 
    get_rental_by_id, 
    update_rental,
    get_all_rentals,
    get_rental_by_id,
    get_rentals_by_user,
    get_rentals_by_movie
)


def calculate_late_fee(checkout_date, checkin_date):
    days_used = (checkin_date - checkout_date).days

    if days_used <= 7:
        return 0

    late_days = days_used - 7
    return late_days * 5

def checkout_movie(user_id, movie_id, provider_id, base_price):
    rental = Rental(
        user_id=user_id,
        movie_id=movie_id,
        provider_id=provider_id,
        checkout_date=date.today(),
        base_price=base_price,
        status="RENTED"
    )

    return save_rental(rental)

def return_movie(rental_id):
    rental = get_rental_by_id(rental_id)

    if not rental or rental.status == "RETURNED":
        return None

    rental.checkin_date = date.today()

    late_fee = calculate_late_fee(
        rental.checkout_date,
        rental.checkin_date
    )

    rental.late_fee = late_fee
    rental.total_price = rental.base_price + late_fee
    rental.status = "RETURNED"

    update_rental()
    return rental

def fetch_all_rentals():
    return get_all_rentals()

def fetch_rental(rental_id):
    return get_rental_by_id(rental_id)

def fetch_rentals_by_user(user_id):
    return get_rentals_by_user(user_id)

def fetch_rentals_by_movie(movie_id):
    return get_rentals_by_movie(movie_id)
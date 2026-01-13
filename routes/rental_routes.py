from flask import Blueprint, request, jsonify
from services.rental_service import (
    checkout_movie,
    return_movie,
    fetch_all_rentals,
    fetch_rental,
    fetch_rentals_by_user,
    fetch_rentals_by_movie
)

rental_bp = Blueprint("rental", __name__)


@rental_bp.route("/checkout", methods=["POST"])
def checkout():
    data = request.json

    rental = checkout_movie(
        user_id=data["user_id"],
        movie_id=data["movie_id"],
        provider_id=data["provider_id"],
        base_price=data["price"]
    )

    return jsonify({
        "message": "Movie rented successfully",
        "rental_id": rental.id
    }), 201


@rental_bp.route("/return/<int:rental_id>", methods=["POST"])
def return_movie_api(rental_id):
    rental = return_movie(rental_id)

    if not rental:
        return jsonify({"error": "Invalid or already returned rental"}), 400

    return jsonify({
        "message": "Movie returned successfully",
        "late_fee": float(rental.late_fee),
        "total_price": float(rental.total_price)
    }), 200


@rental_bp.route("", methods=["GET"])
def get_rentals():
    rentals = fetch_all_rentals()
    return jsonify([r.to_dict() for r in rentals])


@rental_bp.route("/<int:rental_id>", methods=["GET"])
def get_rental(rental_id):
    rental = fetch_rental(rental_id)
    if not rental:
        return jsonify({"error": "Rental not found"}), 404
    return jsonify(rental.to_dict())


@rental_bp.route("/user/<int:user_id>", methods=["GET"])
def get_rentals_by_user_api(user_id):
    rentals = fetch_rentals_by_user(user_id)
    return jsonify([r.to_dict() for r in rentals])


@rental_bp.route("/movie/<int:movie_id>", methods=["GET"])
def get_rentals_by_movie_api(movie_id):
    rentals = fetch_rentals_by_movie(movie_id)
    return jsonify([r.to_dict() for r in rentals])

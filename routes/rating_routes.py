from flask import Blueprint, request, jsonify
from services.rating_service import create_rating, get_movie_ratings

rating_bp = Blueprint("ratings", __name__)

@rating_bp.route("/movies/<int:movie_id>/ratings", methods=["POST"])
def add_rating(movie_id):
    create_rating(movie_id, request.json)
    return jsonify({"message": "Rating added"}), 201

@rating_bp.route("/movies/<int:movie_id>/ratings", methods=["GET"])
def get_ratings(movie_id):
    ratings = get_movie_ratings(movie_id)

    if not ratings:
        return jsonify({"message": "No ratings found for this movie"}), 404

    return jsonify([r.to_dict() for r in ratings]), 200

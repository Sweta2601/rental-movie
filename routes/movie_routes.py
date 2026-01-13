from flask import Blueprint, request, jsonify
from services.movie_service import *
# from utils.auth import is_valid_user

movie_bp = Blueprint("movies", __name__)

# Register movie
@movie_bp.route("/movies", methods=["POST"])
def add_movie():
    movie = create_movie(request.json)
    return jsonify(movie.to_dict()), 201

# Search / list movies
@movie_bp.route("/movies", methods=["GET"])
def get_movies():
    name = request.args.get("name")
    movies = list_movies(name)
    return jsonify([m.to_dict() for m in movies])



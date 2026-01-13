from models.movie import Movie
from repositories.movie_repo import (
    save_movie,
    get_all_movies,
    search_movie
)
from repositories.rating_repo import get_ratings_by_movie_id
from repositories.user_repo import get_user_by_id

def create_movie(data):
    movie = Movie(
        title=data["title"],
        price=data["price"],
        provider_id=data["provider_id"]
    )
    save_movie(movie)
    return movie

def list_movies(name=None):
    if name:
        return search_movie(name)
    return get_all_movies()


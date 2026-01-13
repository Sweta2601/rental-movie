from repositories.rating_repo import save_rating, get_ratings_by_movie_id
from models.rating import Rating
from utils.validators import validate_rating
from utils.errors import ValidationError

def create_rating(movie_id, data):
    if "rating" not in data or "user_id" not in data:
        raise ValidationError("Rating and user_id are required")

    validate_rating(data["rating"])

    rating = Rating(
        movie_id=movie_id,
        user_id=data["user_id"],
        rating=data["rating"],
        review=data.get("review")
    )
    
    save_rating(rating)
    return rating

def get_movie_ratings(movie_id):
    return get_ratings_by_movie_id(movie_id)
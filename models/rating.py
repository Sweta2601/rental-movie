from database.db import db

class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    rating = db.Column(db.Integer)
    review = db.Column(db.String(300))

    def to_dict(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "review": self.review
        }

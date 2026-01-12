from database.db import db

class Movie(db.Model):
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String(50))
    release_year = db.Column(db.Integer)

    provider_id = db.Column(db.Integer, db.ForeignKey("providers.id")) 

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "genre": self.genre,
            "release_year": self.release_year,
            "provider_id": self.provider_id
        }

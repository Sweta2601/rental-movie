from datetime import date
from database.db import db

class Rental(db.Model):
    __tablename__ = "rentals"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey("providers.id"), nullable=False)

    checkout_date = db.Column(db.Date, nullable=False, default=date.today)
    checkin_date = db.Column(db.Date)

    base_price = db.Column(db.Numeric(10, 2), nullable=False)
    late_fee = db.Column(db.Numeric(10, 2), default=0)
    total_price = db.Column(db.Numeric(10, 2))

    status = db.Column(db.String(20), default="RENTED")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "provider_id": self.provider_id,
            "checkout_date": self.checkout_date.isoformat(),
            "checkin_date": self.checkin_date.isoformat() if self.checkin_date else None,
            "base_price": self.base_price,
            "late_fee": self.late_fee,
            "total_price": self.total_price,
            "status": self.status
        }
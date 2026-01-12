from database.db import db

class Provider(db.Model):
    __tablename__ = "providers"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "store_name": self.store_name}

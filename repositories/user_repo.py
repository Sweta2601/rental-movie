from models.user import User
from database.db import db
from utils.errors import DatabaseError

def save_user(user: User):
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        raise DatabaseError("Failed to save user to database") from e

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def search_user_by_name(name):
    return User.query.filter(User.name.ilike(f"%{name}%")).all()

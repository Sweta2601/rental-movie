from repositories.user_repo import *
from models.user import User
from utils.errors import ValidationError



def create_user(data):
    if not data.get("name"):
        raise ValidationError("User name is required")

    user = User(
        name=data["name"],
        is_active=True
    )

    save_user(user)
    return user

def list_users(name=None):
    if name:
        return search_user_by_name(name)
    return get_all_users()

def fetch_user(user_id):
    return get_user_by_id(user_id)

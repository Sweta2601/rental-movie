from models.user import User

def is_valid_user(user_id):
    user = User.query.get(user_id)
    return user and user.is_active

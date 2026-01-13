from flask import Blueprint, request, jsonify
from services.user_service import create_user, list_users, fetch_user

user_bp = Blueprint("users", __name__)

# CREATE user (REGISTER)
@user_bp.route("/users", methods=["POST"])
def register_user():
    user = create_user(request.json)
    return jsonify(user.to_dict()), 201

@user_bp.route("/users", methods=["GET"])
def get_users():
    name = request.args.get("name")
    users = list_users(name)
    return jsonify([u.to_dict() for u in users])

@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = fetch_user(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())

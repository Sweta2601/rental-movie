from flask import Blueprint, request, jsonify
from services.provider_service import (
    create_provider,
    list_providers,
    fetch_provider
)

provider_bp = Blueprint("providers", __name__)

# CREATE provider
@provider_bp.route("/providers", methods=["POST"])
def add_provider():
    provider = create_provider(request.json)
    return jsonify(provider.to_dict()), 201


# READ providers (list + search)
@provider_bp.route("/providers", methods=["GET"])
def get_providers():
    name = request.args.get("name")
    providers = list_providers(name)
    return jsonify([p.to_dict() for p in providers]), 200


# READ provider + movies
@provider_bp.route("/providers/<int:id>", methods=["GET"])
def get_provider(id):
    provider, movies = fetch_provider(id)

    if not provider:
        return jsonify({"error": "Provider not found"}), 404

    return jsonify({
        "provider": provider.to_dict(),
        "movies": [m.to_dict() for m in movies]
    }), 200

from repositories.provider_repo import (
    get_all_providers,
    get_provider_by_id,
    search_provider_by_name,
    save_provider
)
from repositories.movie_repo import get_movies_by_provider
from models.provider import Provider

def create_provider(data):
    # Basic validation
    if not data or "store_name" not in data:
        raise ValueError("Provider store_name is required")

    provider = Provider(
        store_name=data["store_name"]
    )

    save_provider(provider)
    return provider

def list_providers(name=None):
    if name:
        return search_provider_by_name(name)
    return get_all_providers()


def fetch_provider(provider_id):
    provider = get_provider_by_id(provider_id)

    if not provider:
        return None, None

    movies = get_movies_by_provider(provider_id)
    return provider, movies

from models.provider import Provider
from database.db import db

def save_provider(provider):
    db.session.add(provider)
    db.session.commit()


def get_all_providers():
    return Provider.query.all()

def get_provider_by_id(provider_id):
    return Provider.query.get(provider_id)

def search_provider_by_name(name):
    return Provider.query.filter(
        Provider.store_name.ilike(f"%{name}%")
    ).all()

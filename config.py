import os

class Config:
    # Format: mysql+pymysql://username:password@host/database_name
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://appuser:app123@localhost/movie_rental_db?local_infile=1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
from flask import Flask
from config import Config
from database.db import db

from routes.user_routes import user_bp
from routes.provider_routes import provider_bp
from routes.movie_routes import movie_bp
from routes.rating_routes import rating_bp
from routes.rental_routes import rental_bp

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
    else:
        app.config.from_object("config.Config")

    @app.route("/")
    def hello_world():
        return "app is running!"

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(provider_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(rating_bp)
    app.register_blueprint(rental_bp, url_prefix="/rentals")


    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

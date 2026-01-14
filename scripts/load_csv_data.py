import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask
from sqlalchemy import text
from database.db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_csv(table_name, file_name, columns, disable_keys=False):
    file_path = os.path.join(DATA_DIR, file_name)
    file_path = file_path.replace("\\", "/")

    try:
        if disable_keys:
            db.session.execute(text(f"ALTER TABLE {table_name} DISABLE KEYS"))

        sql = f"""
        LOAD DATA LOCAL INFILE '{file_path}'
        INTO TABLE {table_name}
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\\n'
        IGNORE 1 LINES
        ({columns});
        """

        db.session.execute(text(sql))
        db.session.commit()

    finally:
        if disable_keys:
            db.session.execute(text(f"ALTER TABLE {table_name} ENABLE KEYS"))
            db.session.commit()

    print(f"Loaded {file_name} into {table_name}")


with app.app_context():
    try:
        print("Starting bulk data load...")

        # Disable FK checks for speed + safety
        db.session.execute(text("SET FOREIGN_KEY_CHECKS=0"))

        # ORDER MATTERS
        load_csv("providers", "providers.csv", "id,store_name")
        load_csv("users", "users.csv", "id,name,email,is_active")

        load_csv(
            "movie",
            "movies.csv",
            "id,title,price,provider_id,genre,release_year",
            disable_keys=True
        )

        load_csv(
            "ratings",
            "ratings.csv",
            "id,movie_id,user_id,rating,review",
            disable_keys=True
        )

        # Commit everything at once
        db.session.commit()

        print(" ALL DATA LOADED SUCCESSFULLY")

    except Exception as e:
        db.session.rollback()
        print(" ERROR DURING DATA LOAD")
        print(str(e))
        sys.exit(1)

    finally:
        # Always re-enable FK checks
        db.session.execute(text("SET FOREIGN_KEY_CHECKS=1"))
        db.session.commit()
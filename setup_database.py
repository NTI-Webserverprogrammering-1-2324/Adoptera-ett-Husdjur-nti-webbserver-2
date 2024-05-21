# setup_database.py
from init import app, db
from models import Name

# Skapa alla tabeller i databasen
with app.app_context():
    db.create_all()
    print("All tables created.")
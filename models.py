# models.py
from init import db

# Definiera en modell för namn, med en ID-kolumn och en namn-kolumn
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unik identifierare
    name = db.Column(db.String(80), nullable=False)  # Namn, får inte vara null
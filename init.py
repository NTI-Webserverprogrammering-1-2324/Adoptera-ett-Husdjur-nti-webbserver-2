# init.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Skapa en Flask-applikation
app = Flask(__name__)

# Konfigurera databasen URI och andra inställningar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'the-day-of-the-saxon'

# Initiera SQLAlchemy med applikationen
db = SQLAlchemy(app)
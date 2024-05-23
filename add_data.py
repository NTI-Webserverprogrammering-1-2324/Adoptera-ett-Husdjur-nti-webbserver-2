from init import app, db
from models import User

# Skapa några namnobjekt
user1 = User(username=form.username.dat, email=form.email.data)

user2 = User(username=form.username.data, email=form.email.data)

# Lägg till namnen i databasen och spara ändringarna
with app.app_context():
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Data added successfully.")
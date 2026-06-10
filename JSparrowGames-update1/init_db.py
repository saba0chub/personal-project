from ext import app, db
from models import Game, Review, User

with app.app_context():

    db.create_all()

    admin = User(username="admin",
                 password="adminpass",
                 role="Admin")
    admin.create()

from main import db

class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    kind = db.Column(db.String)
    breed = db.Column(db.String)
    age = db.Column(db.String)
    shelter_id = db.Column(db.Integer)

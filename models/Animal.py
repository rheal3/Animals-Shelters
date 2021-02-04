from main import db

class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    kind = db.Column(db.String, nullable=False)
    breed = db.Column(db.String)
    age = db.Column(db.String)
    shelter_id = db.Column(db.Integer, db.ForeignKey("shelters.id"), nullable=False)

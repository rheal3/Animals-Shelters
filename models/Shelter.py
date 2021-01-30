from main import db

class Shelter(db.Model):
    # name table has in database
    __tablename__ = "shelters"

    # each column in shelters table & datatype to be entered
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)

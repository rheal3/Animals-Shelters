from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Animal import Animal
    from models.Shelter import Shelter
    import random

    shelters = []

    for i in range(5):
        shelter = Shelter()
        shelter.name = f"Shelter {i}"
        shelter.email = f"test{i}@email.com"
        shelter.phone = "000000000"
        shelter.address = f"{i} Bilbi Street"
        shelter.city = "Shelter City {i}"
        db.session.add(shelter)
        shelters.append(shelter)

    db.session.commit()

    for i in range(15):
        animal = Animal()
        animal.name = f"Animal{i}"
        animal.kind = f"Kind{i}"
        animal.breed = f"Breed{i}"
        animal.age = f"{i + 13} weeks"
        animal.shelter_id = random.choice(shelters).id
        db.session.add(animal)
    
    db.session.commit()
    print("Tables seeded")
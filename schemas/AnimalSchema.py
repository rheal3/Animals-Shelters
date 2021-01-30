from main import ma
from models.Animal import Animal


class AnimalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Animal


animal_schema = AnimalSchema()
animals_schema = AnimalSchema(many=True)

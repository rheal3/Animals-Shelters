from main import ma
from models.Shelter import Shelter

# model has to be able to serialize and deserialize that's why schema is needed (to help turn into json)
class ShelterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shelter                                                             # based on shelter model


shelter_schema = ShelterSchema()
shelters_schema = ShelterSchema(many=True)
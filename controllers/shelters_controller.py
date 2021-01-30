from models.Shelter import Shelter
from main import db
from schemas.ShelterSchema import shelter_schema, shelters_schema
from flask import Blueprint, request, jsonify

shelters = Blueprint("shelters", __name__, url_prefix="/shelters")                  # create blueprint for shelters

@shelters.route("/", methods=["GET"])                                               # create route for shelter
def shelter_index():
    """
        Returns index of all shelters.
    """
    shelters = Shelter.query.all()                                                  # same as select * from shelters, accesses through model->db
    return jsonify(shelters_schema.dump(shelters))                                  # convert shelters query result into json using shelters_schema

@shelters.route("/", methods=["POST"])
def create_shelter():
    """
        Create a new shelter.
    """
    shelter_fields = shelter_schema.load(request.json)                              # info sent to site from user (insomnia request)
    
    new_shelter = Shelter()                                                         # create new shelter object from model & fill with data from request
    
    new_shelter.name = shelter_fields["name"]
    new_shelter.email = shelter_fields["email"]
    new_shelter.phone = shelter_fields["phone"]
    new_shelter.address = shelter_fields["address"]
    new_shelter.city = shelter_fields["city"]
    
    db.session.add(new_shelter)                                                     # add new_shelter to database
    db.session.commit()                                                             # commit added data to database
    return jsonify(shelter_schema.dump(new_shelter))
from models.Shelter import Shelter
from models.Animal import Animal
from schemas.AnimalSchema import animals_schema
from main import db
from schemas.ShelterSchema import shelter_schema, shelters_schema
from flask import Blueprint, request, jsonify, render_template
from models.Shelter import ShelterForm

shelters = Blueprint("shelters", __name__, url_prefix="/shelters")                  # create blueprint for shelters

@shelters.route("/", methods=["GET"])                                               # create route for shelter
def shelter_index():
    """
        Returns index of all shelters.
    """
    shelters = Shelter.query.all()                                                  # same as select * from shelters, accesses through model->db
    # return jsonify(shelters_schema.dump(shelters))                                  # convert shelters query result into json using shelters_schema
    return render_template("shelter_index.html", shelters=shelters)                 # renders template using html file to website

# @shelters.route("/", methods=["POST"])
# def shelter_create():
#     """
#         Create a new shelter.
#     """
#     shelter_fields = shelter_schema.load(request.json)                              # info sent to site from user (insomnia request)
    
#     new_shelter = Shelter()                                                         # create new shelter object from model & fill with data from request
#     new_shelter.name = shelter_fields["name"]
#     new_shelter.email = shelter_fields["email"]
#     new_shelter.phone = shelter_fields["phone"]
#     new_shelter.address = shelter_fields["address"]
#     new_shelter.city = shelter_fields["city"]
    
#     db.session.add(new_shelter)                                                     # add new_shelter to database
#     db.session.commit()                                                             # commit added data to database
#     return jsonify(shelter_schema.dump(new_shelter))                                # converts to json using schema

@shelters.route('/create', methods=['GET', 'POST'])
def shelter_create():
    form = ShelterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return 'Shelter Added!'
    return render_template('shelter_create.html', form=form)

@shelters.route("/<int:id>", methods=["GET"])
def shelter_show(id):
    """
        Show data for single shelter using id.
    """
    shelter = Shelter.query.get(id)                                                 # query single shelter using id
    # return jsonify(shelter_schema.dump(shelter))                                    # converts to json using schema & returns json data                              
    return render_template("shelter_show.html", shelter=shelter)

@shelters.route("/<int:id>", methods=["DELETE"])
def shelter_delete(id):
    """
        Delete shelter from database using id.
    """
    shelter = Shelter.query.get(id)                                                 # get shelter to delete
    if not shelter:
        return "DELETED"
    db.session.delete(shelter)                                                      # delete from db
    db.session.commit()                                                             # commit changes to db session
    return jsonify(shelter_schema.dump(shelter))                                    # return deleted shelter

@shelters.route("/<int:id>", methods=["PUT", "PATCH"])
def shelter_update(id):
    """
        Update shelter data using id.
    """
    shelter = Shelter.query.filter_by(id=id)                                        # filter_by returns an array of elements by default
    shelter_fields = shelter_schema.load(request.json)                              # load shelter fields using schema from user request (insomnia request)
    shelter.update(shelter_fields)                                                  # update shelter with requested data from shelter_fields
    db.session.commit()                                                             # commit data to db session
    return jsonify(shelter_schema.dump(shelter[0]))

@shelters.route("/<int:id>/animals", methods=["GET"])
def shelter_animals_index(id):
    """
    Index of all animals at shelter using id.
    """
    animals = Animal.query.filter_by(shelter_id=id)
    # return jsonify(animals_schema.dump(animals))
    return render_template("animal_index.html", animals=animals )

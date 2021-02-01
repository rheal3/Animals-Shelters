from models.Animal import Animal
from main import db
from schemas.AnimalSchema import animal_schema, animals_schema
from flask import Blueprint, request, jsonify, render_template
from forms.animal_form import AnimalForm

animals = Blueprint("animals", __name__, url_prefix="/animals")

@animals.route("/", methods=["GET"])
def animal_index():
    """
    Returns index of all animals.
    """
    animals = Animal.query.all()
    # return jsonify(animals_schema.dump(animals))
    return render_template("animal_index.html", animals=animals)

# @animals.route("/", methods=["POST"])
# def animal_create():
#     """
#     Create new animal.
#     """
#     animal_fields = animal_schema.load(request.json)

#     new_animal = Animal()
#     new_animal.name = animal_fields["name"]
#     new_animal.kind = animal_fields["kind"]
#     new_animal.breed = animal_fields["breed"]
#     new_animal.age = animal_fields["age"]
#     new_animal.shelter_id = animal_fields["shelter_id"]

#     db.session.add(new_animal)
#     db.session.commit()
#     return jsonify(animal_schema.dump(new_animal))

@animals.route('/create', methods=['GET', 'POST'])
def animal_create():
    form = AnimalForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return 'Animal Added!'
    return render_template('animal_create.html', form=form)

@animals.route("/<int:id>", methods=["GET"])
def animal_show(id):
    """
    Show single animal using id.
    """
    animal = Animal.query.get(id)
    # return jsonify(animal_schema.dump(animal))
    return render_template("animal_show.html", animal=animal)

@animals.route("/<int:id>", methods=["DELETE"])
def animal_delete(id):
    """
    Delete animal from database using id.
    """
    animal = Animal.query.get(id)
    if not animal:
        return "DELETED"
    db.session.delete(animal)
    db.session.commit()
    return jsonify(animal_schema.dump(animal))

@animals.route("/<int:id>", methods=["PUT", "PATCH"])
def animal_update(id):
    """
    Update animal using id.
    """
    animal = Animal.query.filter_by(id=id)
    animal_fields = animal_schema.load(request.json)
    animal.update(animal_fields)
    db.session.commit()
    return jsonify(animal_schema.dump(animal[0]))
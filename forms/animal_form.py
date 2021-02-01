from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm

class AnimalForm(FlaskForm):
    name = StringField('Animal Name', [validators.DataRequired()])
    kind = StringField('Animal Kind', [validators.DataRequired()])
    breed = StringField('Animal Breed', [validators.DataRequired()])
    age = StringField('Animal Age', [validators.DataRequired()])
    shelter_id = StringField('Shelter ID', [validators.DataRequired()])
    submit = SubmitField('Submit')

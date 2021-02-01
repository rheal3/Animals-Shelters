from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form

class AnimalForm(Form):
    name = StringField('Animal Name', [validators.DataRequired()])
    kind = StringField('Animal Kind', [validators.DataRequired()])
    breed = StringField('Animal Breed', [validators.DataRequired()])
    age = StringField('Animal Age', [validators.DataRequired()])
    submit = SubmitField('Submit')

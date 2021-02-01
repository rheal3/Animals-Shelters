from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form

class ShelterForm(Form):
    name = StringField('Shelter Name', [validators.DataRequired()])
    email = StringField('Shelter Email', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    phone = StringField('Shelter Phone', [validators.DataRequired()])
    address = StringField('Shelter Address', [validators.DataRequired()])
    city = StringField('Shelter City', [validators.DataRequired()])
    submit = SubmitField('Submit')

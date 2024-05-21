# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Definiera ett formulär för att lägga till namn
class SignForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])  # Namnfält, obligatoriskt
    submit = SubmitField('Sign')  # Skicka-knapp
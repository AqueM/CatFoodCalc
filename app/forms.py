from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField
from wtforms.validators import InputRequired


class CalcForm(FlaskForm):
    weight = DecimalField("Cat's weight (kg)", validators=[InputRequired()])
    # activity = PasswordField('Password', validators=[InputRequired()])

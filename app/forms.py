from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField, FormField
from wtforms.validators import NumberRange, InputRequired, NoneOf

from app import labels

default = {"default": "-- Please choose an option --"}
activities = default | labels.activity_labels
activities = activities.items()
ages = default | labels.age_labels
ages = ages.items()


class CatForm(FlaskForm):
    weight = DecimalField("Cat's weight (kg)",
                          validators=[InputRequired(message=labels.weight_error),
                                      NumberRange(min=0, max=40, message=labels.weight_invalid_error)],
                          render_kw={"placeholder": "Enter your cat's weight"})
    activity = SelectField("Cat's activity level", choices=activities,
                           validators=[NoneOf(default, message="Please choose a value.")])
    age = SelectField("Cat's age", choices=ages, validators=[NoneOf(default, message="Please choose a value.")])


class FoodForm(FlaskForm):
    protein = DecimalField("Protein %",
                           validators=[InputRequired(message=labels.nutrition_empty_error),
                                       NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                           render_kw={"placeholder": "As per packaging label"})
    fat = DecimalField("Fat %", validators=[InputRequired(message=labels.nutrition_empty_error),
                                            NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                       render_kw={"placeholder": "As per packaging label"})
    fibre = DecimalField("Fibre %", validators=[InputRequired(message=labels.nutrition_empty_error),
                                                NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                         render_kw={"placeholder": "As per packaging label"})
    ash = DecimalField("Ash %", validators=[InputRequired(message=labels.nutrition_empty_error),
                                            NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                       render_kw={"placeholder": "As per packaging label"})
    moisture = DecimalField("Moisture %",
                            validators=[NumberRange(min=0, max=100, message=labels.moisture_invalid_error)],
                            render_kw={"placeholder": "As per packaging label"})


class CalcForm(FlaskForm):
    cat = FormField(CatForm)
    food = FormField(FoodForm)
    submit = SubmitField('Calculate')

from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField, BooleanField, FormField
from wtforms.validators import NumberRange, NoneOf, Optional, InputRequired, DataRequired

from app import labels

default = {"default": "-- Please choose an option --"}
activities = default | labels.activity_labels
activities = activities.items()
ages = default | labels.age_labels
ages = ages.items()

food_data = ["protein", "fat", "fibre", "ash", "moisture"]
food_quality_data = ["grains", "grains3", "plants", "plants3", "organs", "byproducts", "vitamins", "taurine",
                     "preservatives"]


# Field names must match CatData(Enum)
class CatDataForm(FlaskForm):
    weight = DecimalField("Cat's weight (kg)",
                          validators=[InputRequired(message=labels.weight_error),
                                      NumberRange(min=labels.min_weight, max=labels.max_weight,
                                                  message=labels.weight_invalid_error)],
                          render_kw={"placeholder": "Enter your cat's weight"})
    activity = SelectField("Cat's activity level", choices=activities,
                           validators=[InputRequired(message=labels.list_error),
                                       NoneOf(default, message=labels.list_error)])
    age = SelectField("Cat's age", choices=ages, validators=[InputRequired(message=labels.list_error),
                                                             NoneOf(default, message=labels.list_error)])
    submit_cat = SubmitField('Calculate cat needs >>')


# Field names must match Nutrition(Enum) or FoodRatings(Enum)
class FoodDataForm(FlaskForm):
    protein = DecimalField("Protein %",
                           validators=[InputRequired(message=labels.nutrition_empty_error),
                                       NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                           render_kw={"placeholder": labels.placeholder_package})
    fat = DecimalField("Fat %", validators=[InputRequired(message=labels.nutrition_empty_error),
                                            NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                       render_kw={"placeholder": labels.placeholder_package})
    fibre = DecimalField("Fibre %", validators=[InputRequired(message=labels.nutrition_empty_error),
                                                NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                         render_kw={"placeholder": labels.placeholder_package})
    ash = DecimalField("Ash %", validators=[InputRequired(message=labels.nutrition_empty_error),
                                            NumberRange(min=0, max=100, message=labels.nutrition_invalid_error)],
                       render_kw={"placeholder": labels.placeholder_package})
    moisture = DecimalField("Moisture %",
                            validators=[NumberRange(min=0, max=100, message=labels.moisture_invalid_error), Optional()],
                            render_kw={"placeholder": labels.placeholder_package})
    mass = DecimalField("Package size (g)",
                        validators=[NumberRange(min=0, max=40000, message=labels.moisture_invalid_error), Optional()],
                        render_kw={"placeholder": labels.placeholder_package})
    grains = BooleanField("Ingredients include grains or potatoes", validators=[Optional()])
    grains3 = BooleanField("Grains/potatoes are within first 3 ingredients on the list", validators=[Optional()])
    plants = BooleanField("Ingredients include other vegetables or fruit", validators=[Optional()])
    plants3 = BooleanField("Vegetables/fruit are within first 3 ingredients on the list", validators=[Optional()])
    organs = BooleanField("Ingredients include organs/variety meats", validators=[Optional()])
    byproducts = BooleanField("Ingredients include animal by-products", validators=[Optional()])
    vitamins = BooleanField("Ingredients include vitamins and minerals")
    taurine = BooleanField("Ingredients include taurine")
    preservatives = BooleanField("Ingredients include preservatives")
    submit_food = SubmitField('Calculate all >>')

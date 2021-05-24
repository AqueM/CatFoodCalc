from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField, FormField, BooleanField
from wtforms.validators import NumberRange, NoneOf, Optional, InputRequired

from app import labels

default = {"default": "-- Please choose an option --"}
activities = default | labels.activity_labels
activities = activities.items()
ages = default | labels.age_labels
ages = ages.items()

food_data = ["protein", "fat", "fibre", "ash", "moisture"]
food_quality = ["grains", "grains3", "plants", "plants3", "organs", "byproducts", "vitamins", "taurine",
                "preservatives"]


# Field names must match CatData(Enum)
class CatData(FlaskForm):
    weight = DecimalField("Cat's weight (kg)",
                          validators=[InputRequired(message=labels.weight_error),
                                      NumberRange(min=labels.min_weight, max=labels.max_weight,
                                                  message=labels.weight_invalid_error)],
                          render_kw={"placeholder": "Enter your cat's weight"})
    activity = SelectField("Cat's activity level", choices=activities,
                           validators=[NoneOf(default, message="Please choose a value."), InputRequired()])
    age = SelectField("Cat's age", choices=ages, validators=[NoneOf(default, message="Please choose a value."),
                                                             InputRequired()])


class CatForm(FlaskForm):
    cat = FormField(CatData)
    submit_cat = SubmitField('Calculate cat needs >>')


# Field names must match Nutrition(Enum)
class FoodData(FlaskForm):
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
                            validators=[NumberRange(min=0, max=100, message=labels.moisture_invalid_error), Optional()],
                            render_kw={"placeholder": "As per packaging label"})
    mass = DecimalField("Package size (g)",
                        validators=[NumberRange(min=0, max=40000, message=labels.moisture_invalid_error), Optional()],
                        render_kw={"placeholder": "As per packaging label"})


# Field names must match FoodRatings(Enum)
class FoodQualityForm(FlaskForm):
    grains = BooleanField("Ingredients include grains or potatoes", validators=[Optional()])
    grains3 = BooleanField("Grains/potatoes are within first 3 ingredients on the list", validators=[Optional()])
    plants = BooleanField("Ingredients include other vegetables or fruit", validators=[Optional()])
    plants3 = BooleanField("Vegetables/fruit are within first 3 ingredients on the list", validators=[Optional()])
    organs = BooleanField("Ingredients include organs/variety meats", validators=[Optional()])
    byproducts = BooleanField("Ingredients include animal by-products", validators=[Optional()])
    vitamins = BooleanField("Ingredients include vitamins and minerals")
    taurine = BooleanField("Ingredients include taurine")
    preservatives = BooleanField("Ingredients include preservatives")


class FoodForm(FlaskForm):
    # food = FormField(FoodData)
    # quality = FormField(FoodQualityForm)
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
                            validators=[NumberRange(min=0, max=100, message=labels.moisture_invalid_error), Optional()],
                            render_kw={"placeholder": "As per packaging label"})
    mass = DecimalField("Package size (g)",
                        validators=[NumberRange(min=0, max=40000, message=labels.moisture_invalid_error), Optional()],
                        render_kw={"placeholder": "As per packaging label"})
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
    data_fields = []
    quality_fields = []
    for input in food_data:
        data_fields.append(eval(input))
    for input in food_quality:
        quality_fields.append(eval(input))

from pprint import pprint

from flask import url_for
from werkzeug.utils import redirect

import app.labels as labels
from app import flask_app, render_template, request, forms
from app.calculators import cat_calc, food_calc, rating_calc
from app.enums import Range, ProteinNeeds, CatData, CatAges, CatActivities
from app.forms import FoodDataForm, CatDataForm
from app.reference_data.food_requirements import fat_needs_dry_mass, carbs_needs_dry_mass

basic = {'title': labels.project_title,
         'year': labels.display_years()}
weight_keyword = CatData.weight.value
age_keyword = CatData.age.value
activity_keyword = CatData.activity.value

cat_data = {}
food_data = {}
quality_data = {}


@flask_app.route("/", methods=["GET", "POST"])
def calculator():
    cat_data_input_form = CatDataForm(request.form)
    if cat_data_input_form.validate_on_submit():
        for key, value in cat_data_input_form.data.items():
            cat_data[key] = value
        return redirect(url_for('food_calculator', **locals() | basic))
    return render_template("cat_calc_form.html", **locals() | basic)


@flask_app.route("/food_data-calc", methods=["GET", "POST"])
def food_calculator():
    if cat_data is None or cat_data is False:
        return render_template("error.html", **basic)
    range_min = Range.min
    range_max = Range.max
    range_avg = Range.avg
    bw = ProteinNeeds.bodyweight
    dm = ProteinNeeds.dry_mass
    fat_needs = fat_needs_dry_mass
    carb_needs = carbs_needs_dry_mass
    food_input_form = FoodDataForm(request.form)

    weight = float(cat_data[weight_keyword])
    age = CatAges[eval(cat_data[age_keyword]).name]
    activity = CatActivities[eval(cat_data[activity_keyword]).name]
    age_label = labels.age_labels[age]
    activity_label = labels.activity_labels[activity]

    cat = cat_calc.Cat(float(cat_data[weight_keyword]),
                       CatActivities[eval(cat_data[activity_keyword]).name],
                       CatAges[eval(cat_data[age_keyword]).name])

    if food_input_form.validate_on_submit():
        for key, value in food_input_form.data.items():
            if key == 'csrf_token' or key == 'submit_food':
                continue
            if value is not None:
                if key in forms.food_data:
                    food_data[key] = str(value)
                if key in forms.food_quality_data:
                    quality_data[key] = bool(value)
        return redirect(url_for('results', **locals() | basic))
    return render_template("food_calc_form.html", **locals() | basic)


@flask_app.route("/results", methods=["GET", "POST"])
def results():
    food = food_calc.Food(**food_data)
    cat = cat_calc.Cat(cat_data[weight_keyword],
                       CatActivities[eval(cat_data[activity_keyword]).name],
                       CatAges[eval(cat_data[age_keyword]).name])
    rating = rating_calc.FoodRating(cat, food, quality_data)

    mark = rating.food_rating
    explanation = rating.comments
    return render_template("results.html", **locals() | basic)


@flask_app.route("/about")
def about():
    return render_template("about.html", **locals() | basic)

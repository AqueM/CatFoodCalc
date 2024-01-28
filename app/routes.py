from pprint import pprint

from flask import url_for, session
from werkzeug.utils import redirect

import app.labels as labels
from app import flask_app, render_template, request
from app.calculators import cat_calc, food_calc, rating_calc
from app.enums import Range, ProteinNeeds
from app.forms import FoodDataForm, CatDataForm
from app.reference_data.food_requirements import fat_needs_dry_mass, carbs_needs_dry_mass

basic = {'title': labels.project_title,
         'year': labels.display_years()}


@flask_app.route("/", methods=["GET", "POST"])
def calculator():
    cat_data_input_form = CatDataForm(request.form)
    if cat_data_input_form.validate_on_submit():
        cat_data = {}
        for key, value in cat_data_input_form.data.items():
            cat_data[key] = str(value)
        # session['cat'] = [str(cat_data_input_form.weight.data),
        #                  cat_data_input_form.age.data, cat_data_input_form.activity.data]
        return redirect(url_for('food_calculator', **locals() | basic))
    return render_template("cat_calc_form.html", **locals() | basic)


@flask_app.route("/food_data-calc", methods=["GET", "POST"])
def food_calculator(**kwargs):
    if kwargs.items.cat_data is None or kwargs.items.cat_data is False:
        print("right method wrong if")
        return render_template("error.html", **basic)
    range_min = Range.min
    range_max = Range.max
    range_avg = Range.avg
    bw = ProteinNeeds.bodyweight
    dm = ProteinNeeds.dry_mass
    fat_needs = fat_needs_dry_mass
    carb_needs = carbs_needs_dry_mass
    food_input_form = FoodDataForm(request.form)

    weight = float(kwargs.items.cat_data['weight'])
    age_label = labels.age_labels[eval(kwargs.items.cat_data['age'])]
    activity_label = labels.activity_labels[eval(kwargs.items.cat_data['activity'])]

    if food_input_form.validate_on_submit():
        food_data = {}
        for key, value in food_input_form.data.items():
            if value is not None:
                food_data[key] = str(value)
        pprint(food_input_form.food.data.items())
        pprint(food_input_form.quality.data.items())
        quality = food_input_form.quality.data
        return redirect(url_for('results', **locals() | basic))
    return render_template("food_calc_form.html", **locals() | basic)


@flask_app.route("/results", methods=["GET", "POST"])
def results(**kwargs):
    # session['quality'].pop('csrf_token')
    # session['food'].pop('csrf_token')
    # food_data = {}
    # for key, value in session['food'].items():
    #     food_data[key] = float(value)

    weight = float(kwargs.items.cat_data['weight'])
    age = eval(kwargs.items.cat_data['age'])
    age_label = labels.age_labels[age]
    activity = eval(kwargs.items.cat_data['activity'])
    activity_label = labels.activity_labels[activity]
    cat = cat_calc.Cat(weight, age, activity)

    food = food_calc.Food(kwargs.items.food_data)
    rating = rating_calc.FoodRating(cat, food, kwargs.items.quality)

    mark = rating.food_rating
    return render_template("results.html", **locals() | basic)


@flask_app.route("/about")
def about():
    return render_template("about.html", **locals() | basic)

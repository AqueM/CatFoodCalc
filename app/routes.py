from pprint import pprint

from flask import url_for, session
from werkzeug.utils import redirect

import app.labels as labels
from app import flask_app, render_template, request
from app.calculators import cat_calc, food_calc, rating_calc
from app.enums import Range, ProteinNeeds, CatAges, CatActivities
from app.reference_data.food_requirements import fat_needs_dry_mass, carbs_needs_dry_mass
from app.forms import FoodForm, CatForm
import app.forms

basic = {'title': labels.project_title,
         'year': labels.display_years()}


@flask_app.route("/", methods=["GET", "POST"])
def calculator():
    form = CatForm(request.form)
    if form.submit_cat.data and form.validate_on_submit():
        cat = {}
        for key, value in form.cat.data.items():
            cat[key] = str(value)
        session['cat'] = cat
        # session['cat'] = [str(form.cat.weight.data), form.cat.age.data, form.cat.activity.data]
        return redirect(url_for('food_calculator'))
    return render_template("cat_calc_form.html", **locals() | basic)


@flask_app.route("/food-calc", methods=["GET", "POST"])
def food_calculator():
    if 'cat' not in session:
        return render_template("error.html", **locals() | basic)
    range_min = Range.min
    range_max = Range.max
    range_avg = Range.avg
    bw = ProteinNeeds.bodyweight
    dm = ProteinNeeds.dry_mass
    fat_needs = fat_needs_dry_mass
    carb_needs = carbs_needs_dry_mass
    form = FoodForm(request.form)

    weight = float(session['cat']['weight'])
    age = eval(session['cat']['age'])
    age_label = labels.age_labels[age]
    activity = eval(session['cat']['activity'])
    activity_label = labels.activity_labels[activity]
    cat = cat_calc.Cat(**session['cat'])
    if form.validate_on_submit():
        food = {}
        for key, value in form.data.items():
            if value is not None:
                food[key] = str(value)
        session['food'] = food
        pprint(form.food.data.items())
        pprint(form.quality.data.items())
        session['quality'] = form.quality.data
        return redirect(url_for('results'))
    return render_template("food_calc_form.html", **locals() | basic)


@flask_app.route("/results", methods=["GET", "POST"])
def results():
    session['quality'].pop('csrf_token')
    session['food'].pop('csrf_token')
    food_data = {}
    for key, value in session['food'].items():
        food_data[key] = float(value)

    cat = cat_calc.Cat(**session['cat'])
    food = food_calc.Food(**food_data)
    rating = rating_calc.FoodRating(cat, food, **session['quality'])

    mark = rating.food_rating
    return render_template("results.html", **locals() | basic)


@flask_app.route("/about")
def about():
    return render_template("about.html", **locals() | basic)

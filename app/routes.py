from flask import url_for
from werkzeug.utils import redirect

import app.labels as labels
import app.reference_data.food_requirements as reqs
from app import flask_app, render_template, request, forms
from app.calculators import cat_calc, food_calc, rating_calc
from app.calculators.cat_calc import Cat
from app.calculators.food_calc import Food
from app.enums import CatAges, CatActivities, Range, ProteinNeeds
from app.forms import FoodDataForm, CatDataForm

context = {'title': labels.project_title,
           'year': labels.display_years()}

cat_data = []
cat = Cat
food = Food
quality_data = {}


@flask_app.route("/", methods=["GET", "POST"])
def calculator():
    global cat_data
    cat_data_input_form = CatDataForm(request.form)
    if cat_data_input_form.validate_on_submit():
        for key, value in cat_data_input_form.data.items():
            if key == 'csrf_token' or key == 'submit_cat':
                continue
            cat_data.append(value)
        return redirect(url_for('food_calculator', **context))
    return render_template("cat_calc_form.html", **locals(), **context)


@flask_app.route("/food-calc", methods=["GET", "POST"])
def food_calculator():
    global cat
    global food
    if cat_data is None or cat_data is False:
        return render_template("error.html", **context)
    food_input_form = FoodDataForm(request.form)

    weight = cat_data[0]
    activity = CatActivities[cat_data[1]]
    activity_label = labels.activity_labels[activity.name]

    age = CatAges[cat_data[2]]
    age_label = labels.age_labels[age.name]

    cat = cat_calc.Cat(weight=weight, activity=activity, age=age)

    food_data = {}
    global quality_data

    fat_needs = reqs.fat_needs_dry_mass
    carb_needs = reqs.carbs_needs_dry_mass
    protein_needs = [cat.protein_grams_needed[ProteinNeeds.bodyweight], cat.protein_grams_needed[ProteinNeeds.dry_mass]]

    ranges = [Range.min, Range.avg, Range.max]

    if food_input_form.validate_on_submit():
        for key, value in food_input_form.data.items():
            if key == 'csrf_token' or key == 'submit_food':
                continue
            if value is not None:
                if key in forms.food_data:
                    food_data[str(key)] = str(value)
                if key in forms.food_quality_data:
                    quality_data[str(key)] = bool(value)
        print(quality_data)
        food = food_calc.Food(**food_data)
        return redirect(url_for('results',   **context))
    return render_template("food_calc_form.html", cat=cat,
                           **locals() | context)


@flask_app.route("/results", methods=["GET", "POST"])
def results():
    global cat
    global food
    fat_needs = reqs.fat_needs_dry_mass
    carb_needs = reqs.carbs_needs_dry_mass
    protein_needs = [cat.protein_grams_needed[ProteinNeeds.bodyweight], cat.protein_grams_needed[ProteinNeeds.dry_mass]]

    ranges = [Range.min, Range.avg, Range.max]
    food_rating = rating_calc.FoodRating(cat=cat, food=food, quality_data=quality_data)
    return render_template("results.html", cat=cat, food=food,
                           **locals() | context)


@flask_app.route("/about")
def about():
    return render_template("about.html", **context)

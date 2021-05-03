from flask import url_for, session
from werkzeug.utils import redirect

import app.labels as labels
from app import flask_app, render_template, request, cat_calc
from app.enums import Range, ProteinNeeds, CatAges, CatActivities
from app.food_requirements import fat_needs_dry_mass, carbs_needs_dry_mass
from app.forms import FoodForm, CatForm

basic = {'title': labels.project_title,
         'year': labels.display_years()}


@flask_app.route("/", methods=["GET", "POST"])
def calculator():
    form = CatForm(request.form)
    if form.submit_cat.data and form.validate_on_submit():
        session['weight'] = str(form.cat.weight.data)
        session['age'] = form.cat.age.data
        session['activity'] = form.cat.activity.data
        return redirect(url_for('food_calculator'))
    return render_template("cat_calc_form.html", **locals() | basic)


@flask_app.route("/food-calc", methods=["GET", "POST"])
def food_calculator():
    range_min = Range.min
    range_max = Range.max
    range_avg = Range.avg
    bw = ProteinNeeds.bodyweight
    dm = ProteinNeeds.dry_mass
    fat_needs = fat_needs_dry_mass
    carb_needs = carbs_needs_dry_mass

    form = FoodForm(request.form)
    if ('weight' and 'age' and 'activity') not in session:
        return render_template("error.html", **locals() | basic)
    weight = float(session['weight'])
    age = eval(session['age'])
    age_label = labels.age_labels[age]
    activity = eval(session['activity'])
    activity_label = labels.activity_labels[activity]
    cat = cat_calc.Cat(weight, age, activity)
    if form.food.validate_on_submit() and form.quality.validate_on_submit():
        food = [str(form.food.protein.data), str(form.food.fat.data),
                str(form.food.fibre.data), str(form.food.ash.data),
                str(form.food.moisture.data), str(form.food.mass.data)]
        session['protein'] = str(form.food.protein.data)
        session['fat'] = str(form.food.fat.data)
        session['fibre'] = str(form.food.fibre.data)
        session['ash'] = str(form.food.ash.data)
        session['moisture'] = str(form.food.moisture.data)
        session['mass'] = str(form.food.mass.data)
        quality = [form.quality.data]
        return redirect(url_for('results'))
    return render_template("food_calc_form.html", **locals() | basic)


@flask_app.route("/results", methods=["GET", "POST"])
def results():
    return render_template("results.html", **locals() | basic)


@flask_app.route("/about")
def about():
    return render_template("about.html", **locals() | basic)

from flask import Flask, render_template, flash, request, get_flashed_messages

import app.enums as enums
import app.labels as labels
from app import cat_calc as calc
from app.food_requirements import fat_needs_dry_mass, carbs_needs_dry_mass

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def index():
    inputs = labels.input_labels
    default = {"default": labels.default_dropdown_label}
    ages = default | labels.age_labels
    ages = ages.items()
    activities = default | labels.activity_labels
    activities = activities.items()

    numbers_labels = labels.numbers_labels
    tooltips = labels.tooltips
    title = labels.project_title

    range_min = enums.Range.min
    range_max = enums.Range.max
    der = enums.NumberNames.der
    mer = enums.NumberNames.mer
    daily = labels.per_day
    dm_label = labels.dm_label

    protein_labels = labels.requirements_tooltips
    bw = enums.ProteinNeeds.bodyweight
    dm = enums.ProteinNeeds.dry_mass

    fat_needs = fat_needs_dry_mass
    carb_needs = carbs_needs_dry_mass


    if request.method == "POST":
        if validate_cat_weight(request.form["weight"]):
            weight = request.form["weight"]
        if validate_cat_age(request.form["age"]):
            age = eval("enums." + str(request.form["age"]))
        if validate_cat_activity(request.form["activity"]):
            activity = eval("enums." + str(request.form["activity"]))
        if not get_flashed_messages():
            cat = calc.Cat(weight, age, activity)

    return render_template("index.html", **locals())


def validate_cat_age(age):
    result = True
    if age == "default":
        flash(labels.age_empty_error, 'error')
        result = False
    return result


def validate_cat_activity(activity):
    result = True
    if activity == "default":
        flash(labels.activity_empty_error, 'error')
        result = False
    return result


def validate_cat_weight(weight):
    result = True
    if not weight:
        flash(labels.weight_empty_error, 'error')
        result = False
    else:
        try:
            weight = float(weight)
        except ValueError:
            flash(labels.weight_invalid_error.format(weight), 'error')
            result = False
    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

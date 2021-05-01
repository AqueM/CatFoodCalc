import app.labels as labels
from app import flask_app, render_template, request
from app.enums import Range, NumberNames, ProteinNeeds
from app.flask_validations import validate_food, validate_cat, validate_moisture
from app.food_requirements import fat_needs_dry_mass, carbs_needs_dry_mass
from app.forms import CalcForm


@flask_app.route("/", methods=["GET", "POST"])
def calculator():
    inputs = labels.input_labels
    default = {"default": "-- Please choose an option --"}
    ages = default | labels.age_labels
    ages = ages.items()
    activities = default | labels.activity_labels
    activities = activities.items()

    numbers_labels = labels.numbers_labels
    tooltips = labels.tooltips
    title = labels.project_title

    range_min = Range.min
    range_max = Range.max
    range_avg = Range.avg
    der = NumberNames.der
    mer = NumberNames.mer
    daily = labels.per_day
    dm_label = labels.dm_label

    protein_labels = labels.requirements_tooltips
    bw = ProteinNeeds.bodyweight
    dm = ProteinNeeds.dry_mass

    fat_needs = fat_needs_dry_mass
    carb_needs = carbs_needs_dry_mass
    form = CalcForm()
    year = labels.display_years()

    if request.method == "POST":
        validate_cat()
        protein = request.form["protein"]
        fat = request.form["fat"]
        fibre = request.form["fibre"]
        ash = request.form["ash"]
        moisture = request.form["moisture"]
        validate_food(request.form["protein"],
                      request.form["fat"],
                      request.form["fibre"],
                      request.form["ash"])
        validate_moisture(request.form["moisture"])
    return render_template("calc_form.html", **locals())


@flask_app.route("/about")
def about():
    return render_template("about.html")

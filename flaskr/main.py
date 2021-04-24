from flask import Flask, render_template, flash, request
import flaskr.labels as labels
from flaskr import cat_calc as calc

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def index():
    default = {"default": labels.default_dropdown_label}
    ages = default | labels.age_labels
    ages = ages.items()
    activities = default | labels.activity_labels
    activities = activities.items()
    numbers = labels.numbers_labels
    tooltips = labels.tooltips
    title = labels.project_title

    if request.method == "POST":
        ready = validate_cat_data(request.form["weight"], request.form["age"], request.form["activity"])
        if ready:
            cat = calc.Cat(request.form["weight"], request.form["age"], request.form["activity"])

    return render_template("index.html", **locals())


def validate_cat_data(weight, age, activity):
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
    if age == "default":
        flash(labels.age_empty_error, 'error')
        result = False
    if activity == "default":
        flash(labels.activity_empty_error, 'error')
        result = False

    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

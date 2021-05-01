import app
from app import flash, request, get_flashed_messages, labels, cat_calc


def validate_cat():
    print("cat")
    print(get_flashed_messages(with_categories=True))
    if validate_cat_weight(request.form["weight"]):
        weight = request.form["weight"]
        print(weight)
    if validate_cat_age(request.form["age"]):
        age = eval(request.form["age"])
    if validate_cat_activity(request.form["activity"]):
        activity = eval(request.form["activity"])
    errors = get_flashed_messages(with_categories=True, category_filter="cat")
    print("errors")
    print(errors)
    # if not errors:
        # cat = app.cat_calc.Cat(weight, age, activity)


def validate_cat_age(age):
    result = True
    if age == "default":
        flash(labels.age_empty_error, "cat")
        result = False
    return result


def validate_cat_activity(activity):
    result = True
    if activity == "default":
        flash(labels.activity_empty_error, category="cat")
        result = False
    return result


def validate_cat_weight(weight):
    result = True
    if not weight:
        flash(labels.weight_empty_error, category="cat")
        result = False
    else:
        try:
            weightFloat = float(weight)
        except ValueError:
            flash(labels.weight_invalid_error, category="cat")
            result = False
    return result


def validate_food(*args):
    print("food")
    print(get_flashed_messages(with_categories=True))
    empty = False
    invalid = False
    for i in args:
        if not i:
            empty = True
        else:
            try:
                argument = float(i)
            except ValueError:
                invalid = True
    if empty:
        flash(labels.nutrition_empty_error, category="food")
    if invalid:
        flash(labels.nutrition_invalid_error, category="food")
    print(get_flashed_messages(with_categories=True))


def validate_moisture(moisture):
    try:
        argument = float(moisture)
    except ValueError:
        flash(labels.moisture_invalid_error, category="food")

from datetime import datetime

from app.enums import CatAges, CatActivities, NumberNames, NumberNamesLong, ProteinNeeds, Nutrition

age_labels = {
    CatAges.kitten1.name: "kitten under 4 months",
    CatAges.kitten2.name: "kitten under 9 months",
    CatAges.kitten3.name: "kitten under 12 months",
    CatAges.adult.name: "adult cat",
    CatAges.pregnant.name: "pregnant cat",
    CatAges.mother.name: "lactating cat (under 3 kittens)",
    CatAges.mother3.name: "lactating cat (3+ kittens)"
}
activity_labels = {
    CatActivities.indoor.name: "neutered / inactive / indoor",
    CatActivities.outdoor.name: "active / outdoor"
}
default_dropdown_label = "-- Please choose an option --"

input_labels = {"weight": "Weight (kg)", "weight_placeholder": "Enter the cat's weight", "age": "Age",
                "activity": "Activity level", "submit": "Calculate »",
                "food_placeholder": "As per packaging label",
                Nutrition.protein.value: "Protein %", Nutrition.fat.value: "Fat %", Nutrition.fibre.value: "Fibre %",
                Nutrition.ash.value: "Ash %", Nutrition.moisture.value: "Moisture %"}

max_weight = 50
min_weight = 0.01

weight_error = "Please provide your cat's weight as a decimal number."
weight_invalid_error = "Cat weight must be between {0} and {1} kg.".format(min_weight, max_weight)
list_error = "Please choose a value."
age_empty_error = "Please select your cat's age."
activity_empty_error = "Please select your cat's activity level."
nutrition_empty_error = "Please provide required percentages."
nutrition_invalid_error = "All input values must be numbers, and only numbers (no % needed)."
moisture_invalid_error = "Moisture %% must be a number or left empty."

placeholder_package = "As per package label."


numbers_labels = {NumberNames.der: NumberNamesLong.der.value, NumberNames.mer: NumberNamesLong.mer.value}
tooltips = {
    NumberNames.mer: "Maintenance energy requirement (MER) is the energy required to support energy equilibrium of an "
                     "animal. This does not take growth and reproduction into account.",
    NumberNames.der: "Daily Energy Requirement (DER) is the amount of food energy needed by an animal to "
                     "balance energy expenditure in order to maintain body size, body composition and a level of "
                     "necessary and desirable physical activity consistent with long-term good health."}
per_day = " per day"
dm_label = "daily food's dry mass"

requirements_tooltips = {
    ProteinNeeds.bodyweight: "Calculated from bodyweight",
    ProteinNeeds.dry_mass: "Calculated by " + dm_label
}

project_title = "Cat Food Calculator"


def display_years():
    now = datetime.now().year
    if now != 2021:
        return "2021 - " + str(now)
    else:
        return "2021"

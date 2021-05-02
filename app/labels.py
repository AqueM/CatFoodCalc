from datetime import datetime

from app.enums import CatAges, CatActivities, NumberNames, NumberNamesLong, ProteinNeeds

age_labels = {
    CatAges.kitten1: "kitten under 4 mo",
    CatAges.kitten2: "kitten under 9 mo",
    CatAges.kitten3: "kitten under 12 mo",
    CatAges.adult: "adult cat",
    CatAges.pregnant: "pregnant cat",
    CatAges.mother: "lactating cat (under 3 kittens)",
    CatAges.mother3: "lactating cat (3+ kittens)"
}
activity_labels = {
    CatActivities.indoor: "neutered / inactive / indoor cats",
    CatActivities.outdoor: "active / outdoor cats"
}
default_dropdown_label = "-- Please choose an option --"

input_labels = {"weight": "Weight (kg)", "weight_placeholder": "Enter the cat's weight", "age": "Age",
                "activity": "Activity level", "submit": "Calculate »",
                "food_placeholder": "As per packaging label",
                "protein": "Protein %", "fat": "Fat %", "fibre": "Fibre %", "ash": "Ash %", "moisture": "Moisture %"}

weight_error = "Please provide your cat's weight as a decimal number."
weight_invalid_error = "Cat weight can't be bigger than 50 kg."
age_empty_error = "Please select your cat's age."
activity_empty_error = "Please select your cat's activity level."
nutrition_empty_error = "Please provide required percentages."
nutrition_invalid_error = "All input values must be numbers, and only numbers (no % needed)."
moisture_invalid_error = "Moisture %% must be a number or left empty."

numbers_labels = {NumberNames.der: NumberNamesLong.der.value, NumberNames.mer: NumberNamesLong.mer.value}
tooltips = {
    NumberNames.mer: "Maintenance energy requirement (MER) is the energy required to support energy equilibrium of an "
                     "animal. This does not take growth and reproduction into account.",
    NumberNames.der: "Daily Energy Requirement (DER) is the amount of food energy needed by an animal to "
                     "balance energy expenditure in order to maintain body size, body composition and a level of "
                     "necessary and desirable physical activity consistent with long-term good health."}
per_day = " per day"
dm_label = " daily food's dry mass"

requirements_tooltips = {
    ProteinNeeds.bodyweight: "Calculated from bodyweight",
    ProteinNeeds.dry_mass: "Calculated by" + dm_label
}

project_title = "Cat Food Calculator"


def display_years():
    now = datetime.now().year
    if now != 2021:
        return "2021 - " + str(now)
    else:
        return "2021"

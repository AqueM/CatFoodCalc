# all nutritional values are as detailed in
# FEDIAF Nutritional Guidelines (2019) PDF,
# section 7.2.4. "Practical recommendations for daily energy intake
# by dogs and cats in different physiological states", subsection 7.2.4.2. Cats and table VII-9
# http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf
# http://www.fediaf.org/self-regulation/nutrition.html

kcal_by_activity = {
    "indoor": {"min": 52, "max": 75},
    "outdoor": {"min": 100, "max": 100}
}

age_modifier = {
    "kitten1": {"min": 2, "max": 2.5},
    "kitten2": {"min": 1.75, "max": 2},
    "kitten3": {"min": 1.5, "max": 1.5},
    "adult": {"min": 1, "max": 1},
    "pregnant": {"min": 1.4, "max": 1.4},
    "mother": {"min": 1.2, "max": 1.2},
    "mother3+": {"min": 1.7, "max": 1.7},
}
rer_value = 0.67

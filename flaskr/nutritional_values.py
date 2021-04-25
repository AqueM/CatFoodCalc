# Nutritional requirements as per
# FEDIAF Nutritional Guidelines (2019), as detailed in
# Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
# section 3.2. Tables with nutrient recommendations, subsection 3.2.3.
# Recommended nutrient levels for cats TABLE III-4
# http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf

# Also references FEDIAF Nutrition guide page
# http://www.fediaf.org/self-regulation/nutrition.html
from flaskr.enums import CatActivities, CatAges, Range

kcal_by_activity = {
    CatActivities.indoor: {Range.min: 52, Range.max: 75},
    CatActivities.outdoor: {Range.min: 100, Range.max: 100}
}

age_modifier = {
    CatAges.kitten1: {Range.min: 2, Range.max: 2.5},
    CatAges.kitten2: {Range.min: 1.75, Range.max: 2},
    CatAges.kitten3: {Range.min: 1.5, Range.max: 1.5},
    CatAges.adult: {Range.min: 1, Range.max: 1},
    CatAges.pregnant: {Range.min: 1.4, Range.max: 1.4},
    CatAges.mother: {Range.min: 1.2, Range.max: 1.2},
    CatAges.mother3: {Range.min: 1.7, Range.max: 1.7},
}
rer_value = 0.67


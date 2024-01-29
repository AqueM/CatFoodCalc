# Nutritional requirements as per
# FEDIAF Nutritional Guidelines (2022), as detailed in
# Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
# section 3.2. Tables with nutrient recommendations, subsection 3.2.3.
# Recommended nutrient levels for cats TABLE III-4
# https://europeanpetfood.org/self-regulation/nutritional-guidelines/

from app.enums import CatActivities, CatAges, Range

kcal_by_activity = {
    CatActivities.indoor: {Range.min: 52, Range.max: 75, Range.avg: 0},
    CatActivities.outdoor: {Range.min: 100, Range.max: 100, Range.avg: 0}
}

age_modifier = {
    CatAges.kitten1: {Range.min: 2, Range.max: 2.5, Range.avg: 0},
    CatAges.kitten2: {Range.min: 1.75, Range.max: 2, Range.avg: 0},
    CatAges.kitten3: {Range.min: 1.5, Range.max: 1.5, Range.avg: 0},
    CatAges.adult: {Range.min: 1, Range.max: 1, Range.avg: 0},
    CatAges.pregnant: {Range.min: 1.4, Range.max: 1.4, Range.avg: 0},
    CatAges.mother: {Range.min: 1.2, Range.max: 1.2, Range.avg: 0},
    CatAges.mother3: {Range.min: 1.7, Range.max: 1.7, Range.avg: 0},
}
rer_value = 0.67


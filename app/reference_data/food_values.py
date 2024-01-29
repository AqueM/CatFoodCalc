from app.enums import Nutrition

# Numbers come from
# FEDIAF Nutritional Guidelines(2022),
# as detailed in
# Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
# Table VII-5.
# Predicted gross energy values of protein, fat and carbohydrate
# https://europeanpetfood.org/self-regulation/nutritional-guidelines/

gross_energy_values = {
    Nutrition.protein.value: 5.7,
    Nutrition.fat.value: 9.4,
    Nutrition.fibre.value: 4.1
}

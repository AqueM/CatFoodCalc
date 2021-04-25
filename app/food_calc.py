from app.enums import Nutrition, FoodType


class Food(object):
    # Gross energy as per
    # FEDIAF Nutritional Guidelines (2019), as detailed in
    # Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
    # 7.2.2.1. Gross energy, Table VII-5.
    # Predicted gross energy values of protein, fat and carbohydrate
    # http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf

    gross_energy_values = {
        Nutrition.protein: 5.7,
        Nutrition.carbs: 4.1,
        Nutrition.fat: 9.4,
        Nutrition.fibre: 4.1
    }
    has_energy = [Nutrition.protein, Nutrition.fat, Nutrition.carbs, Nutrition.fibre]

    def __init__(self, protein, fat, fibre, ash, moisture, mass=None):
        self.percentages = {
            Nutrition.protein: protein,
            Nutrition.fat: fat,
            Nutrition.fibre: fibre,
            Nutrition.ash: ash,
            Nutrition.moisture: moisture,
            Nutrition.carbs: self.calculate_carbs()
        }
        if self.percentages[Nutrition.moisture] is not None and self.percentages[Nutrition.moisture] > 0:
            self.food_type = FoodType.wet
        else:
            self.food_type = FoodType.dry
        self.kcal_per_100g = self.calculate_energy()
        self.dry_mass_perc = 100 - self.percentages[Nutrition.moisture]

        if mass is not None and mass > 0:
            self.kcal_whole = (self.kcal_per_100g * mass) / 100

    def calculate_carbs(self):
        return 100 - (sum(value for key, value in self.percentages.items() if key != Nutrition.carbs))

    def calculate_kcal_by_nutrition(self, nutrition):
        return self.percentages[nutrition] * Food.gross_energy_values[nutrition]

    # Formulas and numbers for energy calculation come from
    # FEDIAF Nutritional Guidelines(2019), as detailed in
    # Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
    # 7.2.2.2. Metabolisable energy
    # http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf
    def calculate_energy(self):
        gross_energy = None
        for nutrition in Food.gross_energy_values.keys():
            gross_energy = gross_energy + self.calculate_kcal_by_nutrition(nutrition)

        fibre_dry_mass_perc = (self.percentages[Nutrition.fibre] * self.percentages[Nutrition.moisture]) / 100

        digestibility_modif = 87.9 - (0.88 * fibre_dry_mass_perc)
        digestible_energy = (gross_energy * digestibility_modif) / 100
        metabolic_energy_per_100 = digestible_energy - (0.77 * self.percentages[Nutrition.protein])
        return metabolic_energy_per_100

from app.enums import FoodType, Nutrition
from app.reference_data.food_values import gross_energy_values

protein = Nutrition.protein.value
fat = Nutrition.fat.value
fibre = Nutrition.fibre.value
ash = Nutrition.ash.value
moisture = Nutrition.moisture.value
carbs = Nutrition.carbs.value
mass = 'mass'

has_energy = [protein, fat,
              carbs, fibre]


class Food:
    # Gross energy as per
    # FEDIAF Nutritional Guidelines (2019), as detailed in
    # Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
    # 7.2.2.1. Gross energy, Table VII-5.
    # Predicted gross energy values of protein, fat and carbohydrate
    # http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf

    def __init__(self, **kwargs):
        self.percentages = {protein: float(kwargs[protein]),
                            fat: float(kwargs[fat]),
                            fibre: float(kwargs[fibre]),
                            ash: float(kwargs[ash]),
                            moisture: float(kwargs.get(moisture, 0)),
                            carbs: 0}
        self.food_type = self.get_food_type()
        self.percentages[carbs] = self.calculate_carbs()
        self.kcal_per_100g = self.calculate_digestible_energy_per_100g()
        self.dry_mass_perc = 100 - self.percentages[moisture]
        self.dry_mass_protein = self.calculate_protein_in_100g_dm()
        self.mass = kwargs.get(mass, 0)
        self.kcal_whole = self.calculate_energy_whole()

    def calculate_carbs(self):
        return round(100 - sum(value for key, value in self.percentages.items() if key != carbs), 2)

    def calculate_kcal_gross(self):
        gross_energy = 0
        for food_item in gross_energy_values.keys():
            gross_energy = gross_energy + self.percentages[food_item] * gross_energy_values[food_item]
        return round(gross_energy, 2)

    def get_food_type(self):
        food_type = FoodType.wet
        if self.percentages[moisture] < 10:
            food_type = FoodType.dry
        return food_type

    # Formulas and numbers for energy calculation come from
    # FEDIAF Nutritional Guidelines(2019), as detailed in
    # Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
    # 7.2.2.2. Metabolisable energy
    # http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf
    def calculate_digestible_energy_per_100g(self):
        gross_energy = self.calculate_kcal_gross()

        fibre_dry_mass_perc = \
            (self.percentages[fibre] * self.percentages[moisture]) / 100

        digestibility_modif = 87.9 - (0.88 * fibre_dry_mass_perc)
        digestible_energy = (gross_energy * digestibility_modif) / 100
        metabolic_energy_per_100 = digestible_energy - (0.77 * self.percentages[protein])
        return round(metabolic_energy_per_100, 2)

    def calculate_energy_whole(self):
        if self.mass > 0:
            return self.kcal_per_100g * self.mass / 100
        else:
            return None

    def calculate_protein_in_100g_dm(self):
        return round((100 * self.percentages[protein]) / self.dry_mass_perc, 0)

import statistics

from flaskr.enums import Nutrition, Range


class Food(object):
    kcal_values = {
        Nutrition.protein: 4,
        Nutrition.carbs: 4,
        Nutrition.fat: 9
    }

    def __init__(self, food_type, protein, fat, fibre, ash, moisture, mass=None):
        self.food_type = food_type
        self.percentages = {
            Nutrition.protein: protein,
            Nutrition.fat: fat,
            Nutrition.fibre: fibre,
            Nutrition.ash: ash,
            Nutrition.moisture: moisture,
            Nutrition.carbs: self.calculate_carbs()
        }
        self.kcal_per_100g = self.calculate_kcal_per_100g()
        if mass is not None:
            self.mass = mass
            self.dry_mass = self.calculate_dry_mass()
            self.kcal_whole = self.calculate_kcal_whole()

    def calculate_carbs(self):
        return 100 - (sum(value for key, value in self.percentages.items() if key != Nutrition.carbs))

    def calculate_dry_mass(self):
        return (100 - self.percentages[Nutrition.moisture]) / self.mass

    def calculate_kcal_per_100g(self):
        kcal = {
            Nutrition.protein: self.calculate_kcal_protein(),
            Nutrition.fat: self.calculate_kcal_fat(),
            Nutrition.carbs: self.calculate_kcal_carbs()
        }
        kcal["all"] = sum(kcal.values())
        return kcal

    def calculate_kcal_protein(self):
        return self.percentages[Nutrition.protein] * Food.kcal_values[Nutrition.protein]

    def calculate_kcal_fat(self):
        return self.percentages[Nutrition.fat] * Food.kcal_values[Nutrition.fat]

    def calculate_kcal_carbs(self):
        return self.percentages[Nutrition.carbs] * Food.kcal_values[Nutrition.carbs]

    def calculate_kcal_whole(self):
        kcal_whole = dict()
        for key, value in self.kcal_per_100g:
            kcal_whole[key] = (self.mass * value) / 100
        kcal_whole["all"] = sum(kcal_whole.values())
        return kcal_whole

    def calculate_protein_by_need(self, cat):
        food_grams_by_protein = {
            Range.min: (cat.protein_needs[Range.min] * 100) / self.percentages[Nutrition.protein],
            Range.max: (cat.protein_needs[Range.max] * 100) / self.percentages[Nutrition.protein],
        }
        protein_avg = statistics.mean([food_grams_by_protein[Range.min], food_grams_by_protein[Range.max]])
        protein_avg = round(protein_avg, 2)
        food_grams_by_protein[Range.avg] = protein_avg
        return food_grams_by_protein

    def calculate_kcal_by_need(self, cat):
        food_grams_by_kcal = {
            Range.min: (cat.protein_needs[Range.min] * 100) / self.percentages[Nutrition.protein],
            Range.max: (cat.protein_needs[Range.max] * 100) / self.percentages[Nutrition.protein],
        }
        protein_avg = statistics.mean([food_grams_by_kcal[Range.min], food_grams_by_kcal[Range.max]])
        protein_avg = round(protein_avg, 2)
        food_grams_by_kcal[Range.avg] = protein_avg
        return food_grams_by_kcal


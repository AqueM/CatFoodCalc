from flaskr.enums import ProteinNeeds, Nutrition, Range


class FoodRating(object):
    def __init__(self, cat, food):
        self.cat = cat
        self.food = food
        self.portion_by_protein = self.calculate_grams_by_protein_needs()
        self.portion_by_kcal = self.calculate_grams_by_energy_needs()
        if self.food.kcal_whole is not None:
            self.calculate_package_by_kcal()
        self.food_rating = self.determine_food_quality()

    def calculate_grams_by_protein_needs(self):
        food_grams_by_protein = {
            ProteinNeeds.dry_mass: (self.cat.protein_needs[ProteinNeeds.dry_mass] * 100) / self.percentages[
                Nutrition.protein],
            ProteinNeeds.bodyweight: (self.cat.protein_needs[ProteinNeeds.bodyweight] * 100) / self.percentages[
                Nutrition.protein],
        }
        return food_grams_by_protein

    def calculate_grams_by_energy_needs(self):
        food_grams_by_kcal = {
            Range.min: (self.cat.der[Range.min] * 100) / self.food.kcal_per_100g,
            Range.max: (self.cat.der[Range.max] * 100) / self.food.kcal_per_100g,
        }
        return food_grams_by_kcal

    def determine_kcal_compatibility(self):
        adequate_food = False
        if self.portion_by_kcal[Range.min] >= self.portion_by_protein[ProteinNeeds.bodyweight]:
            adequate_food = True
        if self.portion_by_kcal[Range.min] >= self.portion_by_protein[ProteinNeeds.dry_mass]:
            adequate_food = True
        return adequate_food

    def determine_over_caloric_food(self):
        caloric = False
        if self.portion_by_kcal[Range.max] >= self.portion_by_protein[ProteinNeeds.bodyweight]:
            caloric = True
        if self.portion_by_kcal[Range.max] >= self.portion_by_protein[ProteinNeeds.dry_mass]:
            caloric = True
        return caloric

    def determine_food_quality(self):
        good_food = 0
        if self.determine_kcal_compatibility():
            good_food = good_food + 1
        if self.determine_over_caloric_food:
            good_food = -1
        return good_food

    def calculate_package_by_kcal(self):
        portion_range = {Range.min: self.food.kcal_per_100g/100 * self.portion_by_kcal[Range.min],
                         Range.max: self.food.kcal_per_100g/100 * self.portion_by_kcal[Range.max]}
        return portion_range

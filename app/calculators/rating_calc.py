import pprint

from app.enums import ProteinNeeds, Range, Nutrition, FoodRatings


class FoodRating(object):
    good_values = \
        [FoodRatings.organs.value, FoodRatings.vitamins.value, FoodRatings.taurine.value]
    bad_values = \
        [FoodRatings.grains.value, FoodRatings.grains3.value,
         FoodRatings.plants.value, FoodRatings.plants3.value,
         FoodRatings.byproducts.value, FoodRatings.preservatives.value]

    def __init__(self, cat, food, **kwargs):
        self.cat = cat
        self.food = food
        self.rating_values = {}
        for k, v in kwargs.items():
            self.rating_values[k] = v

        self.portion_by_protein_bw = self.calculate_grams_by_protein_needs_bw()
        self.protein_per_100g_dm = self.calculate_grams_by_protein_needs_dm()

        self.portion_by_kcal = self.calculate_grams_by_energy_needs()

        if self.food.kcal_whole is not None:
            self.calculate_package_by_kcal()

        self.food_rating = self.determine_food_quality()
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(vars(cat))
        # pp.pprint(vars(food))
        # pp.pprint(vars(self))

    def calculate_grams_by_protein_needs_bw(self):
        return (self.cat.protein_needs[ProteinNeeds.bodyweight] * 100) / self.food.percentages[Nutrition.protein]

    def calculate_grams_by_energy_needs(self):
        food_grams_by_kcal = {
            Range.min: (self.cat.der[Range.min] * 100) / self.food.kcal_per_100g,
            Range.max: (self.cat.der[Range.max] * 100) / self.food.kcal_per_100g,
        }
        return food_grams_by_kcal

    def calculate_grams_by_protein_needs_dm(self):
        return (self.food.dry_mass_perc * self.food.percentages[Nutrition.protein]) / 100

    def determine_kcal_compatibility(self):
        adequate_food = False
        if self.portion_by_kcal[Range.min] >= self.portion_by_protein_bw:
            adequate_food = True
        if self.portion_by_kcal[Range.min] >= self.protein_per_100g_dm:
            adequate_food = True
        print("adequate " + str(adequate_food))
        return adequate_food

    def determine_over_caloric_food(self):
        caloric = False
        if self.portion_by_kcal[Range.max] >= self.portion_by_protein_bw:
            caloric = True
        if self.portion_by_kcal[Range.max] >= self.protein_per_100g_dm:
            caloric = True
        print("caloric " + str(caloric))
        return caloric

    def determine_food_quality(self):
        good_food = 0
        if self.determine_kcal_compatibility():
            good_food = good_food + 1
        if self.determine_over_caloric_food():
            good_food = good_food - 1
        for key in self.rating_values.items():
            if key in self.good_values:
                good_food = good_food + 1
            elif key in self.bad_values:
                good_food = good_food - 1
        return good_food

    def calculate_package_by_kcal(self):
        portion_range = {Range.min: self.food.kcal_per_100g / 100 * self.portion_by_kcal[Range.min],
                         Range.max: self.food.kcal_per_100g / 100 * self.portion_by_kcal[Range.max]}
        return portion_range

from app.enums import ProteinNeeds, Range, Nutrition, FoodRatings


class FoodRating():
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

        self.portion_by_kcal = self.calculate_grams_by_energy_needs()

        self.portion_by_protein_bw = self.calculate_grams_by_protein_needs_bw()
        self.portion_by_protein_dm = self.calculate_grams_by_protein_needs_dm()

        if self.food.kcal_whole is not None:
            self.calculate_package_by_kcal()

        self.food_rating = self.determine_food_quality()

    def calculate_grams_by_energy_needs(self):
        food_grams_by_kcal = {
            Range.min: round((self.cat.der[Range.min] * 100) / self.food.kcal_per_100g),
            Range.max: round((self.cat.der[Range.max] * 100) / self.food.kcal_per_100g),
        }
        return food_grams_by_kcal

    def calculate_grams_by_protein_needs_bw(self):
        return round((self.cat.protein_needs[ProteinNeeds.bodyweight] * 100) / self.food.percentages[Nutrition.protein],
                     0)

    def calculate_grams_by_protein_needs_dm(self):
        return round((self.cat.protein_needs[ProteinNeeds.dry_mass] * 100) / self.food.dry_mass_protein)

    def determine_kcal_compatibility(self):
        adequate_food = False
        if self.portion_by_protein_bw >= self.portion_by_kcal[Range.min]:
            adequate_food = True
        if round(self.food.kcal_per_100g / 100, 2) == 4:
            if self.portion_by_protein_dm >= self.portion_by_kcal[Range.min]:
                adequate_food = True
        return adequate_food

    def determine_over_caloric_food(self):
        caloric = False
        if self.portion_by_protein_bw >= self.portion_by_kcal[Range.max]:
            caloric = True
        if self.portion_by_protein_dm >= self.portion_by_kcal[Range.max]:
            caloric = True
        return caloric

    def determine_food_quality(self):
        good_food = 0
        if self.determine_kcal_compatibility():
            good_food = good_food + 1
        if self.determine_over_caloric_food():
            good_food = good_food - 1
        for key in self.rating_values:
            if key in self.good_values:
                good_food = good_food + 1
            elif key in self.bad_values:
                good_food = good_food - 1
        return good_food

    def calculate_package_by_kcal(self):
        if self.food.kcal_whole is not None and self.food.mass < 500:
            return {Range.min: round(self.portion_by_kcal[Range.min] / self.food.mass, 1),
                    Range.max: round(self.portion_by_kcal[Range.max] / self.food.mass, 1)}
        else:
            return None

from app.enums import ProteinNeeds, Range, Nutrition, FoodRatings, FoodType


class FoodRating:
    good_values = \
        [FoodRatings.organs.value, FoodRatings.vitamins.value, FoodRatings.taurine.value]
    bad_values = \
        [FoodRatings.grains.value, FoodRatings.plants.value,
         FoodRatings.byproducts.value, FoodRatings.preservatives.value]
    very_bad_values = \
        [FoodRatings.grains3.value, FoodRatings.plants3.value]
    plant_vars = \
        [FoodRatings.grains.value, FoodRatings.plants.value,
         FoodRatings.grains3.value, FoodRatings.plants3.value]

    too_caloric = ("The food is too caloric for your cat. If aiming for fulfilling the cat's protein needs, "
                   "it may cause weight gain.")
    too_dry = ("The food has too little moisture in it. As cats don't drink much and rely on food for water intake, "
               "this might lead to kidney issues.")
    quality_plants = ("The food has a lot of plants in it. Cats are carnivores and "
                      "do not need plant matter in their diet, "
                      "save for their fibre needs.")
    quality_meat = "The food contains low-quality meat ingredients that are better avoided."
    quality_taurine = ("The food lacks taurine - an essential micronutrient for cats that "
                       "needs to be supplemented for pet cats.")
    portion_comment_empty = "A single package of this food will last for {0} meals for your cat."

    def __init__(self, cat, food, quality_data):
        self.cat = cat
        self.food = food
        self.rating_values = quality_data

        self.portion_by_kcal = self.calculate_grams_by_energy_needs()

        self.portion_by_protein_bw = self.calculate_grams_by_protein_needs_bw()
        self.portion_by_protein_dm = self.calculate_grams_by_protein_needs_dm()

        if self.food.kcal_whole is not None:
            self.calculate_package_by_kcal()

        self.caloric = False
        self.determine_over_caloric_food()
        self.adequate_food = False
        self.determine_kcal_compatibility()
        self.food_rating = self.determine_food_quality()
        self.comments = []
        self.assemble_comments()
        newline = "<br>"
        self.comments = newline.join(self.comments)

        self.portion_comment = ""
        self.portions_per_package = self.calculate_portions()
        if self.portions_per_package is not 0:
            self.portion_comment = self.portion_comment_empty.format(str(self.portions_per_package))

    def calculate_grams_by_energy_needs(self):
        food_grams_by_kcal = {
            Range.min: round((self.cat.der[Range.min] * 100) / self.food.kcal_per_100g),
            Range.max: round((self.cat.der[Range.max] * 100) / self.food.kcal_per_100g),
        }
        return food_grams_by_kcal

    def calculate_grams_by_protein_needs_bw(self):
        return round((self.cat.protein_needs[ProteinNeeds.bodyweight] * 100)
                     / self.food.percentages[Nutrition.protein.value],
                     0)

    def calculate_grams_by_protein_needs_dm(self):
        return round((self.cat.protein_needs[ProteinNeeds.dry_mass] * 100) / self.food.dry_mass_protein)

    def determine_kcal_compatibility(self):
        self.adequate_food = False
        if self.portion_by_protein_bw >= self.portion_by_kcal[Range.min]:
            self.adequate_food = True
        if round(self.food.kcal_per_100g / 100, 2) == 4:
            if self.portion_by_protein_dm >= self.portion_by_kcal[Range.min]:
                self.adequate_food = True

    def determine_over_caloric_food(self):
        if self.portion_by_protein_bw >= self.portion_by_kcal[Range.max]:
            self.caloric = True
        if self.portion_by_protein_dm >= self.portion_by_kcal[Range.max]:
            self.caloric = True

    def determine_food_quality(self):
        food_rating = 5
        if self.adequate_food:
            food_rating += 1
        if self.caloric:
            food_rating -= 1
        if self.food.food_type is FoodType.wet:
            food_rating += 1
        for key in self.rating_values:
            if key in self.good_values:
                food_rating += 1
            elif key in self.bad_values:
                food_rating -= 1
            elif key in self.very_bad_values:
                food_rating -= 2
        return food_rating

    def calculate_package_by_kcal(self):
        if self.food.kcal_whole is not None and self.food.mass < 500:
            return {Range.min: round(self.portion_by_kcal[Range.min] / self.food.mass, 1),
                    Range.max: round(self.portion_by_kcal[Range.max] / self.food.mass, 1)}
        else:
            return None

    def assemble_comments(self):
        if self.food.food_type is not FoodType.wet:
            self.comments += self.too_dry
        if self.caloric is True:
            self.comments += self.too_caloric
        for item in self.plant_vars:
            if item in self.rating_values:
                self.comments += self.quality_plants
                break
        if FoodRatings.byproducts.value in self.rating_values:
            self.comments += self.quality_meat
        if FoodRatings.taurine.value not in self.rating_values:
            self.comments += self.quality_taurine

    def calculate_portions(self):
        self.portions_per_package = 0
        if self.food.mass > 0:
            portions = self.food.mass / self.portion_by_kcal
        else:
            portions = self.food.kcal_whole / self.cat.der[Range.avg]
        return portions

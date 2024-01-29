import statistics

from app.enums import ProteinNeeds, FoodRatings, FoodType, Range, Nutrition, CatActivities
from app.reference_data.food_requirements import adult_protein_needs_100g_drymass

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

not_adequate = ("The food does not have enough protein even in a maximum caloric portion. "
                "This might cause malnutrition if the cat is fed according to calorie needs, "
                "or weight gain if fed according to protein needs. ")
too_dry = ("The food has too little moisture in it. As cats don't drink much and rely on food for water intake, "
           "this might lead to kidney issues. ")
quality_plants = ("The food has a lot of plants in it. Cats are carnivores and "
                  "do not need plant matter in their diet, "
                  "save for their fibre needs. ")
quality_meat = "The food contains low-quality meat ingredients that are better avoided."
quality_taurine = ("The food lacks a taurine source - an essential micronutrient for cats that "
                   "needs to be supplemented for pet cats who don't eat enough variety meats. ")
portion_comment_empty = ("A single {0} package of this food will last {1} days for your cat. "
                         "A daily portion is {2}g.")


class FoodRating:

    def __init__(self, **kwargs):
        self.cat = kwargs['cat']
        self.food = kwargs['food']
        self.rating_values = kwargs['quality_data']

        self.portion_by_kcal = self.calculate_portion_by_energy_needs()
        self.portion_by_protein_bw = self.calculate_portion_by_protein_needs_bw()
        self.portion_by_protein_dm = self.calculate_portion_by_protein_needs_dm()
        self.portion_by_package = self.calculate_portion_as_package_fraction()

        # self.is_caloric = self.determine_too_caloric_food()
        self.has_enough_protein = self.determine_kcal_protein_compatibility()
        self.rating = self.determine_food_quality()
        self.comments_list = self.assemble_comments()

        self.portions_per_package = self.calculate_days_per_package()
        self.portions_per_100g = self.calculate_days_per_100g()
        self.portion_comment = self.assemble_portion_comment()

    def calculate_portion_by_energy_needs(self) -> dict:
        """
        Calculates and sets amount of grams per day needed to fulfil caloric needs

        Returns
        -------
        dict { Range.min: float, Range.max: float, Range.avg: float }
        """
        self.portion_by_kcal = {
            Range.min: round((self.cat.der[Range.min] * 100) / self.food.kcal_100g),
            Range.max: round((self.cat.der[Range.max] * 100) / self.food.kcal_100g),
        }
        self.portion_by_kcal[Range.avg] = round(statistics.mean(
            [self.portion_by_kcal[Range.min],
             self.portion_by_kcal[Range.max]]), 0)
        return self.portion_by_kcal

    def calculate_portion_by_protein_needs_bw(self) -> float:
        """
        Calculates and sets amount of grams per day needed to fulfil protein needs based on body weight

        Returns
        -------
        float
        """
        self.portion_by_protein_bw = (
            round((self.cat.protein_grams_needed[ProteinNeeds.bodyweight] * 100)
                  / self.food.percentages[Nutrition.protein.value],
                  0))
        return self.portion_by_protein_bw

    def calculate_portion_by_protein_needs_dm(self) -> float:
        """
        Calculates and sets amount of grams per day needed to fulfil protein needs based on dry mass

        Returns
        -------
        float
        """
        # calculate how much of the dry mass would fill the dry mass protein requirements
        grams_protein_dm = round((self.cat.protein_grams_needed[ProteinNeeds.dry_mass] * 100)
                                 / self.food.protein_100g_dry_mass, 0)
        # calculate how much food mass will fill the dry mass protein requirements - will be different for wet food
        self.portion_by_protein_dm = round((100 * grams_protein_dm) / self.food.percentage_dry_mass, 0)
        return self.portion_by_protein_dm

    def determine_kcal_protein_compatibility(self) -> bool:
        """
        Sets a bool based on if food has enough protein in a portion by comparing portions by protein
        against maximum portion by kcal.

        Returns
        -------
        bool
        """
        self.has_enough_protein = False
        # check if max portion gives enough protein
        # by body weight
        print("grams to eat to fulfil needs")
        print("dm ", self.portion_by_protein_dm, "bw ", self.portion_by_protein_bw, "kcal min ",
              self.portion_by_kcal[Range.min], "kcal max ", self.portion_by_kcal[Range.max])

        if (self.portion_by_protein_bw <= self.portion_by_kcal[Range.max]) or (
                self.portion_by_protein_dm <= self.portion_by_kcal[Range.max]):
            self.has_enough_protein = True
            if (self.portion_by_kcal[Range.min] > self.portion_by_protein_bw) or (
                    self.portion_by_kcal[Range.min] > self.portion_by_protein_dm):
                print("FAT")

        # if self.portion_by_kcal[Range.min] <= self.portion_by_protein_bw <= self.portion_by_kcal[Range.max]:
        #     self.has_enough_protein = True
        # # by dry mass
        # elif self.portion_by_kcal[Range.min] <= self.portion_by_protein_dm <= self.portion_by_kcal[Range.max]:
        #     self.has_enough_protein = True
        # # for everybody else, min and max values are usually the same, so just check if it has enough protein
        # else:
        #     # check if enough protein by body weight
        #     if self.portion_by_kcal[Range.avg] >= self.portion_by_protein_bw:
        #         self.has_enough_protein = True
        #     # if not, check if enough protein by dry mass
        #     elif self.portion_by_kcal[Range.avg] >= self.portion_by_protein_dm:
        #         self.has_enough_protein = True
        return self.has_enough_protein

    # def determine_too_caloric_food(self) -> bool:
    #     """
    #     Sets a bool based on if food fits the portion range by comparing portions by protein
    #     against maximum portion by kcal
    #
    #     Returns
    #     -------
    #     bool
    #     """
    #     self.is_caloric = False
    #     if self.portion_by_protein_bw > self.portion_by_kcal[Range.max]:
    #         self.is_caloric = True
    #     if self.portion_by_protein_dm > self.portion_by_kcal[Range.max]:
    #         self.is_caloric = True
    #     return self.is_caloric

    def determine_food_quality(self) -> int:
        """
        Increases and decreases an int based on food's protein density, moisture content
         and the rating of ingredients quality

        Returns
        -------
        int between 0 and 10
        """
        food_rating = 5
        if self.has_enough_protein:
            food_rating += 1
        if self.food.food_type is FoodType.wet:
            food_rating += 1
        for key in self.rating_values:
            if key in good_values:  # max +3
                food_rating += 1
            elif key in bad_values:  # max -4
                food_rating -= 1
            elif key in very_bad_values:  # max -2
                food_rating -= 1
        if 0 > food_rating:
            food_rating = 0
        return food_rating

    def calculate_portion_as_package_fraction(self) -> dict | None:
        """
        Calculates and sets the minimum and maximum amount of portions that a package would contain,
        based on portion_by_kcal{}.
        Ignores food objects that has no mass provided or mass is over 500,
        assuming that bigger packages aren't going to be portioned by 'part of package' due to convenience

        Returns
        -------
        dict { Range.min: float, Range.max: float }
        or
        None if mass for food object was not provided or not < 500
        """
        if self.food.kcal_package is not None and self.food.mass < 500:
            return {Range.min: round(self.portion_by_kcal[Range.min] / self.food.mass, 1),
                    Range.max: round(self.portion_by_kcal[Range.max] / self.food.mass, 1)}
        else:
            return None

    def calculate_days_per_package(self) -> float | None:
        """
        Calculates and sets average amount of days that a package will last for,
        based on averaged portion_by_kcal and total package mass.

        Returns
        -------
        float
        or
        None if no mass was provided in food object
        """
        self.portions_per_package = None
        if self.food.kcal_package is not None:
            portions_1 = round(self.food.mass / self.portion_by_kcal[Range.avg], 1)
            portions_2 = round(self.food.kcal_package / self.cat.der[Range.avg], 1)
            if portions_1 == portions_2:
                self.portions_per_package = portions_1
            else:
                self.portions_per_package = round(statistics.mean([portions_1, portions_2]), 1)
        return self.portions_per_package

    def calculate_days_per_100g(self) -> float:
        """
        Calculates and sets average amount of days that 100g will last for,
        based on averaged portion_by_kcal.

        Returns
        -------
        float
        """
        self.portions_per_100g = round(100 / self.portion_by_kcal[Range.avg], 1)
        return self.portions_per_100g

    def assemble_comments(self) -> list[str]:
        """
        Fills out a commentary list based on food properties:
        food_type, is_caloric, has_enough_protein, values in rating_values

        Returns
        -------
        list[str]
        """
        self.comments_list = []
        # dry foods are less healthy
        if self.food.food_type is not FoodType.wet:
            self.comments_list.append(too_dry)
        # foods with too small protein-to-calories ratios are less healthy
        if self.has_enough_protein is False:
            self.comments_list.append(not_adequate)
        # foods with grains or plants are lower quality (less meat)
        for item in plant_vars:
            if item in self.rating_values and self.rating_values[item] is True:
                self.comments_list.append(quality_plants)
                break
        # foods with meat byproducts are lower quality (less meat)
        if (FoodRatings.byproducts.value in self.rating_values
                and self.rating_values[FoodRatings.byproducts.value] is True):
            self.comments_list.append(quality_meat)
        # foods that have no organ ingredients should have added taurine for a taurine source
        if (FoodRatings.organs.value not in self.rating_values
                or self.rating_values[FoodRatings.organs.value] is False):
            if (FoodRatings.taurine.value not in self.rating_values
                    or self.rating_values[FoodRatings.taurine.value] is False):
                self.comments_list.append(quality_taurine)
        # placeholder comment if no other comments are added
        if not self.comments_list:
            self.comments_list.append("A pretty ordinary kind of cat food.")
        return self.comments_list
        # transform into a single string
        # newline = "\n"
        # comments = newline.join(self.comments_list)

    def assemble_portion_comment(self) -> str:
        """
         Sets a comment about the portioning of food

        Returns
        -------
         string
         """
        self.portion_comment = "Couldn't calculate portion information for this food."
        if self.portions_per_package != 0:
            self.portion_comment = (
                portion_comment_empty.format(self.food.mass, str(self.portions_per_package),
                                             str(self.portion_by_kcal[Range.avg])))
        else:
            self.portion_comment = portion_comment_empty.format("100g",
                                                                str(self.portions_per_100g),
                                                                str(self.portion_by_kcal[Range.avg]))
        return self.portion_comment

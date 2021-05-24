import unittest

from app.calculators import rating_calc, cat_calc, food_calc
from app.enums import CatActivities, CatAges, CatData
from tests import test_cat, test_food
from tests.test_base import TestBase


class TestFoodRatingCalculations(TestBase):
    test_data = {
        1: {'cat': cat_calc.Cat(**test_cat.TestCatCalculations.test_data[1]),
            'food': food_calc.Food(**test_food.TestFoodCalculations.test_data["Animonda Carny Multimeat Cocktail"]),
            'grains': True},
        # 2: {CatData.weight.value: 6, CatData.age.value: CatAges.pregnant, CatData.activity.value: CatActivities.outdoor},
        # 3: {CatData.weight.value: 2, CatData.age.value: CatAges.kitten1, CatData.activity.value: CatActivities.outdoor}
    }
    test_results = {1: {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 0,
                        rating_calc.FoodRating.calculate_grams_by_protein_needs_dm: 0,
                        rating_calc.FoodRating.calculate_grams_by_energy_needs: 0,
                        rating_calc.FoodRating.determine_kcal_compatibility: 0,
                        rating_calc.FoodRating.determine_over_caloric_food: 0,
                        rating_calc.FoodRating.determine_food_quality: 0,
                        rating_calc.FoodRating.calculate_package_by_kcal: 0}
                    }

    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = rating_calc.FoodRating
        self.methods_to_test = [rating_calc.FoodRating.calculate_grams_by_protein_needs_bw,
                                rating_calc.FoodRating.calculate_grams_by_protein_needs_dm,
                                rating_calc.FoodRating.calculate_grams_by_energy_needs,
                                rating_calc.FoodRating.determine_kcal_compatibility,
                                rating_calc.FoodRating.determine_over_caloric_food,
                                rating_calc.FoodRating.determine_food_quality,
                                rating_calc.FoodRating.calculate_package_by_kcal]

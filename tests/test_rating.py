import unittest

from app.calculators import rating_calc, cat_calc, food_calc
from app.enums import Range
from tests import test_cat, test_food
from tests.test_base import TestBase


class TestFoodRatingCalculations(TestBase):
    test_data = {
        "medium range wet food": {'cat': cat_calc.Cat(**test_cat.TestCatCalculations.test_data[1]),
                                  'food': food_calc.Food(
                                      **test_food.TestFoodCalculations.test_data["Animonda Carny Multimeat Cocktail"]),
                                  'organs': True},
        "higher end wet food": {'cat': cat_calc.Cat(**test_cat.TestCatCalculations.test_data[2]),
                                'food': food_calc.Food(
                                    **test_food.TestFoodCalculations.test_data["MACs Heart & Liver"]),
                                'taurine': True, 'organs': True, 'vitamins': True},
        "dry kibble": {'cat': cat_calc.Cat(**test_cat.TestCatCalculations.test_data[2]),
                       'food': food_calc.Food(
                           **test_food.TestFoodCalculations.test_data["Purina Pro Plan Adult Urinary Tract "
                                                                      "Health Chicken & Rice Formula"]),
                       'grains': True, 'grains3': True, 'byproducts': True,
                       'taurine': True, 'vitamins': True, 'preservatives': True
                       }
    }
    test_results = {
        "medium range wet food": {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 174,
                                  rating_calc.FoodRating.calculate_grams_by_energy_needs: {Range.min: 131.0,
                                                                                           Range.max: 189.0},
                                  rating_calc.FoodRating.determine_kcal_compatibility: True,
                                  rating_calc.FoodRating.determine_over_caloric_food: False,
                                  rating_calc.FoodRating.determine_food_quality: 2,
                                  rating_calc.FoodRating.calculate_package_by_kcal: {Range.min: 0.3,
                                                                                     Range.max: 0.5}},

        "higher end wet food": {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 500,
                                rating_calc.FoodRating.calculate_grams_by_energy_needs: {Range.min: 478.0,
                                                                                         Range.max: 478.0},
                                rating_calc.FoodRating.determine_kcal_compatibility: True,
                                rating_calc.FoodRating.determine_over_caloric_food: True,
                                rating_calc.FoodRating.determine_food_quality: 3,
                                rating_calc.FoodRating.calculate_package_by_kcal: None},

        "dry kibble": {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 174,
                       rating_calc.FoodRating.calculate_grams_by_energy_needs: {Range.min: 133.0, Range.max: 133.0},
                       rating_calc.FoodRating.determine_kcal_compatibility: True,
                       rating_calc.FoodRating.determine_over_caloric_food: True,
                       rating_calc.FoodRating.determine_food_quality: -2,
                       rating_calc.FoodRating.calculate_package_by_kcal: None}
    }

    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = rating_calc.FoodRating
        self.methods_to_test = [rating_calc.FoodRating.calculate_grams_by_protein_needs_bw,
                                rating_calc.FoodRating.calculate_grams_by_energy_needs,
                                rating_calc.FoodRating.determine_kcal_compatibility,
                                rating_calc.FoodRating.determine_over_caloric_food,
                                rating_calc.FoodRating.determine_food_quality,
                                rating_calc.FoodRating.calculate_package_by_kcal]

import unittest

from app.calculators import rating_calc, cat_calc, food_calc
from app.enums import Range
from tests import test_cat, test_food
from tests.test_base import TestTemplate

test_cases = {
    1: "medium range wet food",
    2: "higher end wet food",
    3: "dry kibble"
}
test_data = {
    1: {'cat': cat_calc.Cat(**test_cat.test_data[1]),
        'food': food_calc.Food(
            **test_food.test_data[1]),
        'quality_data': {'organs': True}},
    2: {'cat': cat_calc.Cat(**test_cat.test_data[2]),
        'food': food_calc.Food(
            **test_food.test_data[2]),
        'quality_data': {'taurine': True, 'organs': True, 'vitamins': True}},
    3: {'cat': cat_calc.Cat(**test_cat.test_data[2]),
        'food': food_calc.Food(
            **test_food.test_data[3]),
        'quality_data': {'grains': True, 'grains3': True, 'byproducts': True,
                         'taurine': True, 'vitamins': True, 'preservatives': True}
        }
}
test_results = {
    1: {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 174,
        rating_calc.FoodRating.calculate_grams_by_protein_needs_dm: 45,
        rating_calc.FoodRating.calculate_grams_by_energy_needs: {Range.min: 131.0,
                                                                 Range.max: 189.0},
        rating_calc.FoodRating.determine_kcal_compatibility: True,
        rating_calc.FoodRating.determine_over_caloric_food: False,
        rating_calc.FoodRating.determine_food_quality: 2,
        rating_calc.FoodRating.calculate_package_by_kcal: {Range.min: 0.3,
                                                           Range.max: 0.5}},

    2: {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 500,
        rating_calc.FoodRating.calculate_grams_by_protein_needs_dm: 67,
        rating_calc.FoodRating.calculate_grams_by_energy_needs: {Range.min: 478.0,
                                                                 Range.max: 478.0},
        rating_calc.FoodRating.determine_kcal_compatibility: True,
        rating_calc.FoodRating.determine_over_caloric_food: True,
        rating_calc.FoodRating.determine_food_quality: 3,
        rating_calc.FoodRating.calculate_package_by_kcal: None},

    3: {rating_calc.FoodRating.calculate_grams_by_protein_needs_bw: 174,
        rating_calc.FoodRating.calculate_grams_by_protein_needs_dm: 97,
        rating_calc.FoodRating.calculate_grams_by_energy_needs: {Range.min: 133.0, Range.max: 133.0},
        rating_calc.FoodRating.determine_kcal_compatibility: True,
        rating_calc.FoodRating.determine_over_caloric_food: True,
        rating_calc.FoodRating.determine_food_quality: -2,
        rating_calc.FoodRating.calculate_package_by_kcal: None}
}


class TestFoodRatingCalculations(TestTemplate):

    def test_methods(self):
        self.test_data = test_data
        self.test_results = test_results
        self.tested_class = rating_calc.FoodRating
        self.methods_to_test = [rating_calc.FoodRating.calculate_grams_by_energy_needs,
                                rating_calc.FoodRating.calculate_grams_by_protein_needs_bw,
                                rating_calc.FoodRating.calculate_grams_by_protein_needs_dm,
                                rating_calc.FoodRating.determine_kcal_compatibility,
                                rating_calc.FoodRating.determine_over_caloric_food,
                                rating_calc.FoodRating.determine_food_quality,
                                rating_calc.FoodRating.calculate_package_by_kcal]
        self.run_methods_test()

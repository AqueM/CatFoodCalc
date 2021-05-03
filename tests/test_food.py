import unittest

from app import food_calc
from app.enums import FoodType
from tests.test_base import TestBase


class TestFoodCalculations(TestBase):
    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = food_calc.Food
        self.methods_to_test = [food_calc.Food.calculate_carbs,
                                food_calc.Food.calculate_kcal_gross,
                                food_calc.Food.calculate_digestible_energy_per_100g,
                                food_calc.Food.get_food_type]
        self.test_data = {
            "Animonda Carny Multimeat Cocktail": [11.5, 6.5, 0.5, 1.8, 79],
            "MACs Heart & Liver": [10.8, 7.2, 0.5, 2.4, 76],
            "Purina Pro Plan Adult Urinary Tract Health Chicken & Rice Formula": [31, 14, 2, 6.2]
        }
        self.test_results = {
            "Animonda Carny Multimeat Cocktail": {
                food_calc.Food.calculate_carbs: 0.7,
                food_calc.Food.calculate_kcal_gross: 131.57,
                food_calc.Food.calculate_digestible_energy_per_100g: 106.34,
                food_calc.Food.get_food_type: FoodType.wet},
            "MACs Heart & Liver": {
                food_calc.Food.calculate_carbs: 3.1,
                food_calc.Food.calculate_kcal_gross: 144,
                food_calc.Food.calculate_digestible_energy_per_100g: 117.78,
                food_calc.Food.get_food_type: FoodType.wet},
            "Purina Pro Plan Adult Urinary Tract Health Chicken & Rice Formula": {
                food_calc.Food.calculate_carbs: 46.8,
                food_calc.Food.calculate_kcal_gross: 508.38,
                food_calc.Food.calculate_digestible_energy_per_100g: 423,
                food_calc.Food.get_food_type: FoodType.dry}
        }

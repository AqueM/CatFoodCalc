import unittest

from app.calculators import food_calc
from app.enums import FoodType, Nutrition
from tests.test_base import TestBase


class TestFoodCalculations(TestBase):
    test_data = {
        "Animonda Carny Multimeat Cocktail":
            {Nutrition.protein.value: 11.5, Nutrition.fat.value: 6.5,
             Nutrition.fibre.value: 0.5, Nutrition.ash.value: 1.8,
             Nutrition.moisture.value: 79},
        "MACs Heart & Liver":
            {Nutrition.protein.value: 10.8, Nutrition.fat.value: 7.2, Nutrition.fibre.value: 0.5,
             Nutrition.ash.value: 2.4, Nutrition.moisture.value: 76},
        "Purina Pro Plan Adult Urinary Tract Health Chicken & Rice Formula":
            {Nutrition.protein.value: 31, Nutrition.fat.value: 14,
             Nutrition.fibre.value: 2, Nutrition.ash.value: 6.2}}
    test_results = {
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

    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = food_calc.Food
        self.methods_to_test = [food_calc.Food.calculate_carbs,
                                food_calc.Food.calculate_kcal_gross,
                                food_calc.Food.calculate_digestible_energy_per_100g,
                                food_calc.Food.get_food_type]

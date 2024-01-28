import unittest

from app.calculators import food_calc
from app.enums import FoodType, Nutrition
from tests.test_base import TestTemplate

protein_keyword = Nutrition.protein.value
fat_keyword = Nutrition.fat.value
fibre_keyword = Nutrition.fibre.value
ash_keyword = Nutrition.ash.value
moisture_keyword = Nutrition.moisture.value
mass_keyword = 'mass'


class TestFoodCalculations(TestTemplate):
    test_cases = {
        1: "Animonda Carny Multimeat Cocktail",
        2: "MACs Heart & Liver",
        3: "Purina Pro Plan Adult Urinary Tract Health Chicken & Rice Formula"
    }
    test_data = {
        test_cases[1]:
            {protein_keyword: 11.5, fat_keyword: 6.5,
             fibre_keyword: 0.5, ash_keyword: 1.8,
             moisture_keyword: 79,
             mass_keyword: 400},
        test_cases[2]:
            {protein_keyword: 10.8, fat_keyword: 7.2, fibre_keyword: 0.5,
             ash_keyword: 2.4, moisture_keyword: 76},
        test_cases[3]:
            {protein_keyword: 31, fat_keyword: 14,
             fibre_keyword: 2, ash_keyword: 6.2, mass_keyword: 1500}}
    test_results = {
        test_cases[1]: {
            food_calc.Food.calculate_carbs: 0.7,
            food_calc.Food.calculate_kcal_gross: 131.57,
            food_calc.Food.calculate_digestible_energy_per_100g: 106.34,
            food_calc.Food.calculate_protein_in_100g_dm: 0,
            food_calc.Food.get_food_type: FoodType.wet},
        test_cases[2]: {
            food_calc.Food.calculate_carbs: 3.1,
            food_calc.Food.calculate_kcal_gross: 144,
            food_calc.Food.calculate_digestible_energy_per_100g: 117.78,
            food_calc.Food.calculate_protein_in_100g_dm: 0,
            food_calc.Food.get_food_type: FoodType.wet},
        test_cases[3]: {
            food_calc.Food.calculate_carbs: 46.8,
            food_calc.Food.calculate_kcal_gross: 508.38,
            food_calc.Food.calculate_digestible_energy_per_100g: 423,
            food_calc.Food.calculate_protein_in_100g_dm: 0,
            food_calc.Food.get_food_type: FoodType.dry}
    }

    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = food_calc.Food
        self.methods_to_test = [food_calc.Food.calculate_carbs,
                                food_calc.Food.calculate_kcal_gross,
                                food_calc.Food.calculate_digestible_energy_per_100g,
                                food_calc.Food.calculate_protein_in_100g_dm,
                                food_calc.Food.get_food_type]

import unittest

from app.calculators import food_calc
from app.enums import FoodType, Nutrition
from tests.test_base import TestTemplate

protein = Nutrition.protein.value
fat = Nutrition.fat.value
fibre = Nutrition.fibre.value
ash = Nutrition.ash.value
moisture = Nutrition.moisture.value
carbs = Nutrition.carbs.value
mass = 'mass'

test_cases = {
    1: "Animonda Carny Multimeat Cocktail",
    2: "MACs Heart & Liver",
    3: "Purina Pro Plan Adult Urinary Tract Health Chicken & Rice Formula"
}
test_data = {
    1:
        {protein: 11.5, fat: 6.5,
         fibre: 0.5, ash: 1.8,
         moisture: 79,
         mass: 400},
    2:
        {protein: 10.8, fibre: 0.5,
         ash: 2.4, fat: 7.2, moisture: 76},
    3:
        {moisture: 0, protein: 31, fat: 14,
         fibre: 2, ash: 6.2, mass: 1500}}
test_results = {
    1: {
        food_calc.Food.calculate_carbs: 0.7,
        food_calc.Food.calculate_kcal_gross_per_100g: 131.57,
        food_calc.Food.calculate_digestible_energy_per_100g: 106.34,
        food_calc.Food.calculate_protein_in_100g_dm: 55,
        food_calc.Food.get_food_type: FoodType.wet},
    2: {
        food_calc.Food.calculate_carbs: 3.1,
        food_calc.Food.calculate_kcal_gross_per_100g: 144,
        food_calc.Food.calculate_digestible_energy_per_100g: 117.78,
        food_calc.Food.calculate_protein_in_100g_dm: 45,
        food_calc.Food.get_food_type: FoodType.wet},
    3: {
        food_calc.Food.calculate_carbs: 46.8,
        food_calc.Food.calculate_kcal_gross_per_100g: 508.38,
        food_calc.Food.calculate_digestible_energy_per_100g: 423,
        food_calc.Food.calculate_protein_in_100g_dm: 31,
        food_calc.Food.get_food_type: FoodType.dry}
}


class TestFoodCalculations(TestTemplate):
    def test_init(self):
        print("Testing class constructor".format(__name__))
        for case in test_cases:
            print("Tested item: {0}... ".format(test_cases[case]), end="")
            food = food_calc.Food(**test_data[case])
            self.assertEqual(food.percentages[protein], test_data[case][protein])
            self.assertEqual(food.percentages[fat], test_data[case][fat])
            self.assertEqual(food.percentages[fibre], test_data[case][fibre])
            self.assertEqual(food.percentages[ash], test_data[case][ash])
            self.assertEqual(food.percentages[moisture], test_data[case][moisture])
            print("PASS")
        print("\n")

    def test_methods(self):
        self.test_data = test_data
        self.test_results = test_results
        self.tested_class = food_calc.Food
        self.methods_to_test = [food_calc.Food.calculate_carbs,
                                food_calc.Food.calculate_kcal_gross_per_100g,
                                food_calc.Food.calculate_digestible_energy_per_100g,
                                food_calc.Food.calculate_protein_in_100g_dm,
                                food_calc.Food.get_food_type]
        self.run_methods_test()


if __name__ == '__main__':
    unittest.main()

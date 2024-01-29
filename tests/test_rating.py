from app.calculators import rating_calc, cat_calc, food_calc
from app.enums import Range
from tests import test_cat, test_food
from tests.test_base import TestTemplate

test_cases = {
    1: "medium range wet food",
    2: "higher end wet food",
    3: "dry kibble",
    4: "decent dry kibble"
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
    3: {'cat': cat_calc.Cat(**test_cat.test_data[3]),
        'food': food_calc.Food(
            **test_food.test_data[3]),
        'quality_data': {'grains3': True, 'plants': True, 'plants3': True,
                         'organs': False, 'byproducts': True, 'vitamins': False,
                         'taurine': True, 'preservatives': True}
        },
    4: {'cat': cat_calc.Cat(**test_cat.test_data[1]),
        'food': food_calc.Food(
            **test_food.test_data[3]),
        'quality_data': {'grains': True, 'grains3': False, 'plants': True, 'plants3': False,
                         'organs': False, 'byproducts': True, 'vitamins': False,
                         'taurine': True, 'preservatives': False}
        }
}
test_results = {
    1: {rating_calc.FoodRating.calculate_portion_by_protein_needs_bw: 174,
        rating_calc.FoodRating.calculate_portion_by_protein_needs_dm: 214,
        rating_calc.FoodRating.calculate_portion_by_energy_needs: {Range.min: 134,
                                                                   Range.max: 194,
                                                                   Range.avg: 164},
        rating_calc.FoodRating.determine_kcal_protein_compatibility: True,
        rating_calc.FoodRating.determine_too_caloric_food: False,
        rating_calc.FoodRating.determine_food_quality: 8,
        rating_calc.FoodRating.calculate_portion_as_package_fraction: {Range.min: 0.3,
                                                                       Range.max: 0.5,
                                                                       Range.avg: 0.4},
        rating_calc.FoodRating.calculate_days_per_package: 2.4,
        rating_calc.FoodRating.calculate_days_per_100g: 0.6},

    2: {rating_calc.FoodRating.calculate_portion_by_protein_needs_bw: 500,
        rating_calc.FoodRating.calculate_portion_by_protein_needs_dm: 279,
        rating_calc.FoodRating.calculate_portion_by_energy_needs: {Range.min: 528,
                                                                   Range.max: 528,
                                                                   Range.avg: 528},
        rating_calc.FoodRating.determine_kcal_protein_compatibility: True,
        rating_calc.FoodRating.determine_too_caloric_food: True,
        rating_calc.FoodRating.determine_food_quality: 10,
        rating_calc.FoodRating.calculate_portion_as_package_fraction: None,
        rating_calc.FoodRating.calculate_days_per_package: None,
        rating_calc.FoodRating.calculate_days_per_100g: 0.2},

    3: {rating_calc.FoodRating.calculate_portion_by_protein_needs_bw: 58,
        rating_calc.FoodRating.calculate_portion_by_protein_needs_dm: 90,
        rating_calc.FoodRating.calculate_portion_by_energy_needs: {Range.min: 105, Range.max: 132, Range.avg: 118},
        rating_calc.FoodRating.determine_kcal_protein_compatibility: True,
        rating_calc.FoodRating.determine_too_caloric_food: True,
        rating_calc.FoodRating.determine_food_quality: 2,
        rating_calc.FoodRating.calculate_portion_as_package_fraction: None,
        rating_calc.FoodRating.calculate_days_per_package: 12.6,
        rating_calc.FoodRating.calculate_days_per_100g: 0.8},

    4: {rating_calc.FoodRating.calculate_portion_by_protein_needs_bw: 65,
        rating_calc.FoodRating.calculate_portion_by_protein_needs_dm: 81,
        rating_calc.FoodRating.calculate_portion_by_energy_needs: {Range.min: 55, Range.max: 79, Range.avg: 67},
        rating_calc.FoodRating.determine_kcal_protein_compatibility: True,
        rating_calc.FoodRating.determine_too_caloric_food: False,
        rating_calc.FoodRating.determine_food_quality: 4,
        rating_calc.FoodRating.calculate_portion_as_package_fraction: None,
        rating_calc.FoodRating.calculate_days_per_package: 22.4,
        rating_calc.FoodRating.calculate_days_per_100g: 1.5}
}


class TestFoodRatingCalculations(TestTemplate):

    def test_methods(self):
        self.test_data = test_data
        self.test_results = test_results
        self.tested_class = rating_calc.FoodRating
        self.methods_to_test = [
            rating_calc.FoodRating.calculate_portion_by_energy_needs,
            rating_calc.FoodRating.calculate_portion_by_protein_needs_bw,
            rating_calc.FoodRating.calculate_portion_by_protein_needs_dm,
            rating_calc.FoodRating.determine_kcal_protein_compatibility,
            rating_calc.FoodRating.determine_too_caloric_food,
            rating_calc.FoodRating.determine_food_quality,
            rating_calc.FoodRating.calculate_portion_as_package_fraction,
            rating_calc.FoodRating.calculate_days_per_package,
            rating_calc.FoodRating.calculate_days_per_100g
        ]
        self.run_methods_test()

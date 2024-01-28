import unittest

from app.calculators import cat_calc
from app.enums import CatActivities, Range, CatAges, ProteinNeeds, CatData
from tests.test_base import TestTemplate

test_cases = {
    1: "basic adult",
    2: "scrambled data pregnant",
    3: "basic kitten"
}

weight = CatData.weight.value
age = CatData.age.value
activity = CatData.activity.value
age_modif = 'age_modif'
is_kitten = 'is_kitten'
rer = 'rer'

test_data = {
    1: {weight: 4, age: CatAges.adult, activity: CatActivities.indoor},
    2: {activity: CatActivities.outdoor, age: CatAges.pregnant, weight: 6},
    3: {weight: 2, age: CatAges.kitten1, activity: CatActivities.outdoor}
}
test_results = {
    1: {cat_calc.Cat.calculate_mer: {Range.min: 139, Range.max: 201, Range.avg: 170},
        cat_calc.Cat.calculate_der: {Range.min: 139, Range.max: 201, Range.avg: 170},
        cat_calc.Cat.calculate_protein_needs:
            {ProteinNeeds.bodyweight: 20,
             ProteinNeeds.dry_mass: 25},
        age_modif: {Range.min: 1, Range.max: 1, Range.avg: 0},
        rer: 2.68,
        is_kitten: False},
    2: {cat_calc.Cat.calculate_mer: {Range.min: 402, Range.max: 402, Range.avg: 402},
        cat_calc.Cat.calculate_der: {Range.min: 563, Range.max: 563, Range.avg: 563},
        cat_calc.Cat.calculate_protein_needs:
            {ProteinNeeds.bodyweight: 54,
             ProteinNeeds.dry_mass: 30},
        age_modif: {Range.min: 1.4, Range.max: 1.4, Range.avg: 0},
        rer: 4.02,
        is_kitten: False},
    3: {cat_calc.Cat.calculate_mer: {Range.min: 134, Range.max: 134, Range.avg: 134},
        cat_calc.Cat.calculate_der: {Range.min: 268, Range.max: 335, Range.avg: 302},
        cat_calc.Cat.calculate_protein_needs:
            {ProteinNeeds.bodyweight: 18,
             ProteinNeeds.dry_mass: 28},
        age_modif: {Range.min: 2, Range.max: 2.5, Range.avg: 0},
        rer: 1.34,
        is_kitten: True}
}


class CatTests(TestTemplate):

    def test_init(self):
        print("Testing class constructor".format(cat_calc.__name__))
        for case in test_cases:
            print("Tested item: {0}... ".format(test_cases[case]), end="")
            cat = cat_calc.Cat(**test_data[case])
            self.assertEqual(cat.weight, test_data[case][weight])
            self.assertEqual(cat.age, test_data[case][age])
            self.assertEqual(cat.activity, test_data[case][activity])
            print("PASS")
        print("\n")

    def test_methods(self):
        self.test_data = test_data
        self.test_results = test_results
        self.tested_class = cat_calc.Cat
        self.methods_to_test = [cat_calc.Cat.calculate_der,
                                cat_calc.Cat.calculate_mer,
                                cat_calc.Cat.calculate_protein_needs]
        self.run_methods_test()

    def test_variables(self):
        print("Testing other class variables for ".format(cat_calc.__name__))
        for case in test_cases:
            print("Tested item: {0}... ".format(test_cases[case]), end="")
            cat = cat_calc.Cat(**test_data[case])
            self.assertEqual(cat.age_modif, test_results[case][age_modif])
            self.assertEqual(cat.rer_formula_by_weight, test_results[case][rer])
            self.assertEqual(cat.is_kitten, test_results[case][is_kitten])
            print("PASS")
        print("\n")


if __name__ == '__main__':
    unittest.main()

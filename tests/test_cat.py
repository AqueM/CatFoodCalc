import unittest

from app.calculators import cat_calc
from app.enums import CatActivities, Range, CatAges, ProteinNeeds, CatData
from tests.test_base import TestBase


class TestCatCalculations(TestBase):
    test_data = {
        1: {CatData.weight.value: 4, CatData.age.value: CatAges.adult, CatData.activity.value: CatActivities.indoor},
        2: {CatData.weight.value: 6, CatData.age.value: CatAges.pregnant,
            CatData.activity.value: CatActivities.outdoor},
        3: {CatData.weight.value: 2, CatData.age.value: CatAges.kitten1, CatData.activity.value: CatActivities.outdoor}}
    test_results = {
        1: {cat_calc.Cat.calculate_mer: {Range.min: 139, Range.max: 201, Range.avg: 170},
            cat_calc.Cat.calculate_der: {Range.min: 139, Range.max: 201, Range.avg: 170},
            cat_calc.Cat.calculate_protein_needs:
                {ProteinNeeds.bodyweight: 20,
                 ProteinNeeds.dry_mass: 25}},
        2: {cat_calc.Cat.calculate_mer: {Range.min: 402, Range.max: 402, Range.avg: 402},
            cat_calc.Cat.calculate_der: {Range.min: 563, Range.max: 563, Range.avg: 563},
            cat_calc.Cat.calculate_protein_needs:
                {ProteinNeeds.bodyweight: 54,
                 ProteinNeeds.dry_mass: 30}},
        3: {cat_calc.Cat.calculate_mer: {Range.min: 134, Range.max: 134, Range.avg: 134},
            cat_calc.Cat.calculate_der: {Range.min: 268, Range.max: 335, Range.avg: 302},
            cat_calc.Cat.calculate_protein_needs:
                {ProteinNeeds.bodyweight: 18,
                 ProteinNeeds.dry_mass: 28}},
    }

    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = cat_calc.Cat
        self.methods_to_test = [cat_calc.Cat.calculate_der,
                                cat_calc.Cat.calculate_mer,
                                cat_calc.Cat.calculate_protein_needs]

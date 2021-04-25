import unittest

from app import cat_calc
from app.enums import CatActivities, Range, NumberNames, CatAges, ProteinNeeds
from tests.test_base import TestBase


class TestBaseCatCalculations(TestBase):
    def __init__(self, method_name='runTest'):
        unittest.TestCase.__init__(self, method_name)
        self.tested_class = cat_calc.Cat
        self.methods_to_test = {NumberNames.der: cat_calc.Cat.calculate_der,
                                NumberNames.mer: cat_calc.Cat.calculate_mer,
                                NumberNames.protein_needs: cat_calc.Cat.calculate_protein_needs}
        self.test_data = {
            1: [4, CatAges.adult, CatActivities.indoor],
            2: [6, CatAges.pregnant, CatActivities.outdoor],
            3: [2, CatAges.kitten1, CatActivities.outdoor]
        }
        self.test_results = {
            1: {NumberNames.mer: {Range.min: 139, Range.max: 201},
                NumberNames.der: {Range.min: 139, Range.max: 201},
                NumberNames.protein_needs:
                    {ProteinNeeds.bodyweight: 20,
                     ProteinNeeds.dry_mass: 25}},
            2: {NumberNames.mer: {Range.min: 402, Range.max: 402},
                NumberNames.der: {Range.min: 563, Range.max: 563},
                NumberNames.protein_needs:
                    {ProteinNeeds.bodyweight: 54,
                     ProteinNeeds.dry_mass: 30}},
            3: {NumberNames.mer: {Range.min: 134, Range.max: 134},
                NumberNames.der: {Range.min: 268, Range.max: 335},
                NumberNames.protein_needs:
                    {ProteinNeeds.bodyweight: 18,
                     ProteinNeeds.dry_mass: 28}},
        }

import unittest
import CatFoodCalc.cat_calc as cat_calc


class TestCatCalculations(unittest.TestCase):
    # weight, age, activity
    data = [[4, 3, 0], [6, 4, 1], [2, 0, 1]]
    cats_data = {}
    # kcal per kg min, kcal per kg max, der min, der max, mer min, mer max
    results = [[52, 75, 139.36, 201, 139.36, 201], [100, 100, 402, 402, 562.8, 562.8], [100, 100, 134, 134, 268, 335]]
    cats_results = {}

    methods_to_test = ["cat_calc.Cat.get_kcal_per_kg_by_activity(tested_cat)[0]",
                       "cat_calc.Cat.get_kcal_per_kg_by_activity(tested_cat)[1]",
                       "cat_calc.Cat.calculate_der(tested_cat)[0]",
                       "cat_calc.Cat.calculate_der(tested_cat)[1]",
                       "cat_calc.Cat.calculate_mer(tested_cat)[0]",
                       "cat_calc.Cat.calculate_mer(tested_cat)[1]"]

    def construct_cats_with_results(self):
        for x in range(len(self.data)):
            self.cats_data[x] = self.data[x]
            self.cats_results[x] = self.results[x]

    def method_base_test(self, methods):
        for tested_function in methods:
            for c, v in self.cats_data.items():
                tested_cat = cat_calc.Cat(v[0], v[1], v[2])
                expected = self.cats_results.get(c)[methods.index(tested_function)]
                unittest.TestCase().assertEqual(eval(tested_function), expected)

    def testMethods(self, methods=methods_to_test):
        self.construct_cats_with_results()
        self.method_base_test(methods)


if __name__ == "__main__":
    unittest.main()

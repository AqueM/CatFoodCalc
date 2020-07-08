import unittest
import CatFoodCalc.cat_calc as cat_calc


class TestCatCalculations(unittest.TestCase):
    test_cats_data = {
        "cat1": [4, "adult", "indoor"],
        "cat2": [6, "pregnant", "outdoor"],
        "cat3": [2, "kitten1", "outdoor"]
    }
    test_cats_results = {
        "cat1": {"der": {"min": 139.36, "max": 201}, "mer": {"min": 139.36, "max": 201}},
        "cat2": {"der": {"min": 402, "max": 402}, "mer": {"min": 562.8, "max": 562.8}},
        "cat3": {"der": {"min": 134, "max": 134}, "mer": {"min": 268, "max": 335}},
    }

    methods_to_test = {"der": "calculate_der",
                       "mer": "calculate_mer"}

    def get_test_results(self, method, used_cat):
        tested_method = "cat_calc.Cat." + str(method) + "(used_cat)"
        result = eval(tested_method)
        return result

    def method_base_test(self, methods):
        for name, function in methods.items():
            for cat, value in self.test_cats_data.items():
                tested_cat = cat_calc.Cat(value[0], value[1], value[2])
                expected = self.test_cats_results[cat][name]
                actual = self.get_test_results(function, tested_cat)
                unittest.TestCase().assertEqual(actual, expected)

    def testMethods(self, methods=methods_to_test):
        self.method_base_test(methods)


if __name__ == "__main__":
    unittest.main()

import unittest


def get_results(method, used_object):
    return method(used_object)


class TestTemplate(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.methods_to_test = []
        self.test_results = {}
        self.test_data = {}
        self.tested_class = str

    def run_methods_test(self):
        self.assertTrue(self.methods_to_test, "No methods provided for testing")
        self.assertTrue(self.test_data, "No test data provided")
        self.assertTrue(self.test_results, "No test results provided")
        for function in self.methods_to_test:
            print("Testing method {0}: ".format(function.__name__))
            self.run_one_method(function, self.tested_class, self.test_data, self.test_results)
            print("\n")

    @staticmethod
    def run_one_method(method, tested_class, test_data, test_results):
        for name, data in test_data.items():
            used_object = tested_class(**data)
            expected = test_results[name][method]
            actual = get_results(method, used_object)
            print("Tested item: {0}... ".format(name), end="")
            unittest.TestCase().assertEqual(expected, actual,
                                            "Failed testing method {0} for test item {1}".format(method.__name__,
                                                                                                 name))
            print("PASS")

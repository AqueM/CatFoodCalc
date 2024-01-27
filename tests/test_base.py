import unittest


def get_results(method, used_object):
    return method(used_object)


def run_one_method(function, tested_class, test_data, test_results):
    for test_object, value in test_data.items():
        used_object = tested_class(**value)
        expected = test_results[test_object][function]
        actual = get_results(function, used_object)
        print("Tested item: {0}... ".format(test_object), end="")
        unittest.TestCase().assertEqual(expected, actual,
                                        "Failed testing method {0} for test item {1}".format(function.__name__,
                                                                                             test_object))
        print("PASS")


class TestTemplate(unittest.TestCase):
    def __init__(self, method_name: str = "runTest"):
        super().__init__(method_name)
        self.test_results = {}
        self.test_data = {}
        self.tested_class = str
        self.methods_to_test = []

    def runTest(self):
        for function in self.methods_to_test:
            print("Testing method {0}: ".format(function.__name__))
            run_one_method(function, self.tested_class, self.test_data, self.test_results)
            print("")

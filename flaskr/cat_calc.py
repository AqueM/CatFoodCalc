from flaskr import nutritional_values
import statistics


class Cat(object):
    def __init__(self, weight, age, activity):
        self.activity = activity
        self.kcal_needs_per_kg = nutritional_values.kcal_by_activity[self.activity]
        self.weight = float(weight)
        self.age = age
        self.age_modif = nutritional_values.age_modifier[self.age]

        # RER - Resting Energy Requirement (by weight only)
        self.rer_formula_by_weight = self.weight * nutritional_values.rer_value

        # MER - Maintenance Energy Requirement (by weight and activity)
        self.mer = self.calculate_mer()
        self.mer_avg = statistics.mean([self.mer["min"], self.mer["max"]])
        self.mer_avg = round(self.mer_avg, 0)

        # DER - Daily Energy Requirement (total, by weight, activity and age)
        self.der = self.calculate_der()
        self.der_avg = statistics.mean([self.der["min"], self.der["max"]])
        self.der_avg = round(self.der_avg, 0)

    def calculate_mer(self):
        mer = {"min": self.rer_formula_by_weight * self.kcal_needs_per_kg["min"],
               "max": self.rer_formula_by_weight * self.kcal_needs_per_kg["max"]}

        mer["min"] = round(mer["min"], 2)
        mer["max"] = round(mer["max"], 2)

        return mer

    def calculate_der(self):
        der = {"min": self.mer["min"] * self.age_modif["min"],
               "max": self.mer["max"] * self.age_modif["max"]}

        der["min"] = round(der["min"], 2)
        der["max"] = round(der["max"], 2)

        return der

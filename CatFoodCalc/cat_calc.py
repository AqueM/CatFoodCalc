from CatFoodCalc import nutritional_values
import statistics


class Cat(object):
    def __init__(self, weight, age, activity):
        self.activity = activity
        self.kcal_needs_per_kg = nutritional_values.kcal_by_activity[self.activity]
        self.weight = weight
        self.age = age
        self.age_modif = nutritional_values.age_modifier[self.age]

        # RER - Resting Energy Requirement (by weight only)
        # '0.67' value taken from a nutritional guide. See nutritional_values.py for reference
        self.rer_formula_by_weight = self.weight * 0.67

        # DER - Daily Energy Requirement (by weight and activity)
        self.der = self.calculate_der()
        self.der_avg = statistics.mean([self.der["min"], self.der["max"]])
        self.der_avg = round(self.der_avg, 0)

        # MER - Metabolic Energy Requirement (total, by weight, activity and age)
        self.mer = self.calculate_mer()
        self.mer_avg = statistics.mean([self.mer["min"], self.mer["max"]])
        self.mer_avg = round(self.mer_avg, 0)

    def calculate_der(self):
        der = {}

        der["min"] = self.rer_formula_by_weight * self.kcal_needs_per_kg["min"]
        der["min"] = round(der["min"], 2)

        der["max"] = self.rer_formula_by_weight * self.kcal_needs_per_kg["max"]
        der["max"] = round(der["max"], 2)

        return der

    def calculate_mer(self):
        mer = {}

        mer["min"] = self.der["min"] * self.age_modif["min"]
        mer["min"] = round(mer["min"], 2)
        mer["max"] = self.der["max"] * self.age_modif["max"]
        mer["max"] = round(mer["max"], 2)

        return mer

import presets

class Cat(object):

    def __init__(self, weight, age, activity):
        self.kcal_per_kg = {
                "outdoor": presets.kcal_per_kg["outdoor"],
                "indoor": presents.kcal_per_kg["indoor"]
            }
        self.weight = weight
        self.age = age
        self.activity = activity
        self.der_formula_by_weight = self.weight * 0.67
        self.der = self.calculate_der()

    def calculate_der(self):
        der = self.der_formula_by_weight * self.get_kcal_per_kg_by_activity()
        der["min"] = round(der["min"], 2)
        der["max"] = round(der["max"], 2)

        return(der)

    def get_kcal_per_kg_by_activity(self):
        kcal_per_kg = {}

        levels_by_activity = self.kcal_per_kg[self.activity]

        kcal_per_kg["min"] = levels_by_activity["min"]
        kcal_per_kg["max"] = levels_by_activity["max"]

        return(kcal_per_kg)

    def get_age_modifier(self):
        # TODO
        pass

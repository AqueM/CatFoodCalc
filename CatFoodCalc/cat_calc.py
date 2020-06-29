class Cat:
    # age = {
    #     1: "kitten under 4 mo",
    #     2: "kitten under 9 mo",
    #     3: "kitten under 12 mo",
    #     4: "adult cat",
    #     5: "pregnant cat",
    #     6: "lactating cat (under 3 kittens)",
    #     7: "lactating cat (3+ kittens)",
    #     8: "senior cat"
    # }
    # activity = {
    #     1: "neutered, inactive and indoor cats",
    #     2: "active and outdoor cats"
    # }

    kcal_per_kg_indoor = [52, 75]
    kcal_per_kg_outdoor = [100]

    def __init__(self, weight, age, activity):
        self.kcal_per_kg_outoor = Cat.kcal_per_kg_outdoor
        self.kcal_per_kg_indoor = Cat.kcal_per_kg_indoor
        self.weight = weight
        self.age = age
        self.activity = activity
        self.der_formula_by_weight = self.weight * 0.67
        self.der = self.calculate_der()

    def calculate_der(self):
        return [round(self.der_formula_by_weight * self.get_kcal_per_kg_by_activity()[0], 2),
                round(self.der_formula_by_weight * self.get_kcal_per_kg_by_activity()[1], 2)]

    def get_kcal_per_kg_by_activity(self):
        if self.activity == 2:
            kcal_per_kg_min = self.kcal_per_kg_outoor[0]
            kcal_per_kg_max = self.kcal_per_kg_outoor[0]
        else:
            kcal_per_kg_min = self.kcal_per_kg_indoor[0]
            kcal_per_kg_max = self.kcal_per_kg_indoor[1]
        return [kcal_per_kg_min, kcal_per_kg_max]

    # def get_age_modifier(self):
    #     # TODO

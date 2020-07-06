import statistics


class Cat:
    # all nutritional values are as detailed in
    # FEDIAF Nutritional Guidelines (2019) PDF,
    # section 7.2.4. "Practical recommendations for daily energy intake
    # by dogs and cats in different physiological states", subsection 7.2.4.2. Cats and table VII-9
    # http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf
    # http://www.fediaf.org/self-regulation/nutrition.html

    age_labels = {
        0: "kitten under 4 mo",
        1: "kitten under 9 mo",
        2: "kitten under 12 mo",
        3: "adult cat",
        4: "pregnant cat",
        5: "lactating cat (under 3 kittens)",
        6: "lactating cat (3+ kittens)"
    }
    activity_labels = {
        0: "neutered / inactive / indoor cats",
        1: "active / outdoor cats"
    }

    kcal_by_activity = [
        [52, 75],
        [100, 100]
    ]

    age_modifier = [
        [2, 2.5],
        [1.75, 2],
        [1.5, 1.5],
        [1, 1],
        [1.4, 1.4],
        [1.2, 1.2],
        [1.7, 1.7]
    ]

    def __init__(self, weight, age, activity):
        self.weight = weight
        self.age = age
        self.activity = activity
        self.age_modif = self.get_age_modifier()
        # RER - Resting Energy Requirement (by weight only)
        self.rer_formula_by_weight = self.weight * 0.67
        # DER - Daily Energy Requirement (by weight and activity)
        self.der = self.calculate_der()
        self.der_avg = round(statistics.mean(self.der), 0)
        # MER - Metabolic Energy Requirement (total, by weight, activity and age)
        self.mer = self.calculate_mer()
        self.mer_avg = round(statistics.mean(self.mer), 0)

    def calculate_der(self):
        return [round(self.rer_formula_by_weight * self.get_kcal_per_kg_by_activity()[0], 2),
                round(self.rer_formula_by_weight * self.get_kcal_per_kg_by_activity()[1], 2)]

    def get_kcal_per_kg_by_activity(self):
        kcal_per_kg_min = self.kcal_by_activity[self.activity][0]
        kcal_per_kg_max = self.kcal_by_activity[self.activity][1]
        return [kcal_per_kg_min, kcal_per_kg_max]

    def get_age_modifier(self):
        return self.age_modifier[self.age]

    def calculate_mer(self):
        mer_min = self.der[0] * self.age_modif[0]
        mer_max = self.der[1] * self.age_modif[1]
        return [mer_min, mer_max]

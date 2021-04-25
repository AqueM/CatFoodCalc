import statistics

import app.enums as enums
from app import nutritional_values, food_requirements


class Cat(object):
    def __init__(self, weight, age, activity):
        self.activity = eval("enums." + str(activity))
        self.kcal_needs_per_kg = nutritional_values.kcal_by_activity[self.activity]
        self.weight = float(weight)
        self.age = eval("enums." + str(age))
        self.age_modif = nutritional_values.age_modifier[self.age]

        # RER - Resting Energy Requirement (by weight only)
        self.rer_formula_by_weight = self.weight * nutritional_values.rer_value

        # MER - Maintenance Energy Requirement (by weight and activity)
        self.mer = self.calculate_mer()
        self.mer_avg = statistics.mean([self.mer[enums.Range.min], self.mer[enums.Range.max]])
        self.mer_avg = round(self.mer_avg, 0)

        # DER - Daily Energy Requirement (total, by weight, activity and age)
        self.der = self.calculate_der()
        self.der_avg = statistics.mean([self.der[enums.Range.min], self.der[enums.Range.max]])
        self.der_avg = round(self.der_avg, 0)
        self.protein_needs = self.calculate_protein_needs()

    def calculate_mer(self):
        mer = {enums.Range.min: self.rer_formula_by_weight * self.kcal_needs_per_kg[enums.Range.min],
               enums.Range.max: self.rer_formula_by_weight * self.kcal_needs_per_kg[enums.Range.max]}

        mer[enums.Range.min] = round(mer[enums.Range.min], 0)
        mer[enums.Range.max] = round(mer[enums.Range.max], 0)
        return mer

    def calculate_der(self):
        der = {enums.Range.min: self.mer[enums.Range.min] * self.age_modif[enums.Range.min],
               enums.Range.max: self.mer[enums.Range.max] * self.age_modif[enums.Range.max]}

        der[enums.Range.min] = round(der[enums.Range.min], 0)
        der[enums.Range.max] = round(der[enums.Range.max], 0)
        return der

    def calculate_protein_needs(self):
        protein_needs = {
            enums.ProteinNeeds.bodyweight: round(food_requirements.protein_needs_bodyweight[self.age] * self.weight, 2),
            enums.ProteinNeeds.dry_mass: food_requirements.protein_needs_dry_mass_by_age[self.age]
        }
        if self.age == enums.CatAges.adult:
            protein_needs[enums.ProteinNeeds.dry_mass] = protein_needs[enums.ProteinNeeds.dry_mass][self.activity]
        protein_needs[enums.ProteinNeeds.dry_mass] = float(round(protein_needs[enums.ProteinNeeds.dry_mass], 2))
        return protein_needs

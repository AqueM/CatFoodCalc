import statistics

from app.reference_data import food_requirements, nutritional_requirements
from app.enums import Range, ProteinNeeds, CatAges, kittens


class Cat:
    def __init__(self, weight, activity, age):
        self.weight = float(weight)
        self.age = age
        self.activity = activity
        self.age_modif = nutritional_requirements.age_modifier[self.age]
        self.kcal_needs_per_kg = nutritional_requirements.kcal_by_activity[self.activity]

        # RER - Resting Energy Requirement (by weight only)
        self.rer_formula_by_weight = round(self.weight * nutritional_requirements.rer_value, 2)

        # MER - Maintenance Energy Requirement (by weight and activity)
        self.mer = self.calculate_mer()

        # DER - Daily Energy Requirement (total, by weight, activity and age)
        self.der = self.calculate_der()

        self.protein_needs = self.calculate_protein_needs()
        self.is_kitten = False
        if self.age in kittens:
            self.is_kitten = True

    def calculate_mer(self):
        mer = dict()
        for key in Range:
            mer[key] = round(self.rer_formula_by_weight * self.kcal_needs_per_kg[key], 0)
        mer[Range.avg] = round(statistics.mean([mer[Range.min], mer[Range.max]]), 0)
        return mer

    def calculate_der(self):
        der = dict()
        for key in Range:
            der[key] = round(self.mer[key] * self.age_modif[key], 0)
        der[Range.avg] = round(statistics.mean([der[Range.min], der[Range.max]]), 0)
        return der

    def calculate_protein_needs(self):
        protein_needs = {
            ProteinNeeds.bodyweight: round(food_requirements.protein_needs_bodyweight[self.age] * self.weight, 2),
            ProteinNeeds.dry_mass: food_requirements.protein_needs_dry_mass_by_age[self.age]
        }
        if self.age == CatAges.adult:
            protein_needs[ProteinNeeds.dry_mass] = protein_needs[ProteinNeeds.dry_mass][self.activity]
        protein_needs[ProteinNeeds.dry_mass] = float(round(protein_needs[ProteinNeeds.dry_mass], 2))
        return protein_needs

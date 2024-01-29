import statistics

from app.reference_data import food_requirements, nutritional_requirements
from app.enums import Range, ProteinNeeds, CatAges, kittens


class Cat:

    def __init__(self, **kwargs):
        self.weight = float(kwargs['weight'])
        self.age = kwargs['age']
        self.activity = kwargs['activity']
        self.age_modif = nutritional_requirements.age_modifier[self.age]
        self.kcal_needs_per_kg = nutritional_requirements.kcal_by_activity[self.activity]

        self.rer_formula_by_weight = self.calculate_rer()
        self.mer = self.calculate_mer()
        self.der = self.calculate_der()

        self.protein_grams_needed = self.calculate_protein_needs()
        self.is_kitten = self.determine_if_kitten()

    def calculate_rer(self) -> float:
        """
        Calculates and sets Resting Energy Requirement by weight and a constant

        Returns
        -------
        float
        """
        self.rer_formula_by_weight = round(self.weight * nutritional_requirements.rer_value, 2)
        return self.rer_formula_by_weight

    def calculate_mer(self) -> dict:
        """
        Calculates and sets MER - Maintenance Energy Requirement by weight and activity

        Returns
        -------
        dict { Range.min: float, Range.max: float, Range.avg: float }
        """
        self.mer = {}
        for key in Range:
            self.mer[key] = round(self.rer_formula_by_weight * self.kcal_needs_per_kg[key], 0)
        self.mer[Range.avg] = round(statistics.mean([self.mer[Range.min], self.mer[Range.max]]), 0)
        return self.mer

    def calculate_der(self) -> dict:
        """
        Calculates and sets DER - Daily Energy Requirement (total) by weight, activity and age

        Returns
        -------
        dict { Range.min: float, Range.max: float, Range.avg: float }
        """
        self.der = dict()
        for key in Range:
            self.der[key] = round(self.mer[key] * self.age_modif[key], 0)
        self.der[Range.avg] = round(statistics.mean([self.der[Range.min], self.der[Range.max]]), 0)
        return self.der

    def calculate_protein_needs(self) -> dict:
        """
        Determines and sets protein needs in grams, based on age and activity.

        Returns
        -------
        dict { ProteinNeeds.bodyweight: float, ProteinNeeds.dry_mass: float }
        """
        # protein needs are mostly based on age
        self.protein_grams_needed = {
            ProteinNeeds.bodyweight: round(food_requirements.protein_needs_bodyweight[self.age] * self.weight, 2),
            ProteinNeeds.dry_mass: food_requirements.protein_needs_drymass_by_age[self.age]
        }
        # adults get more specific info on protein needs based on activity level
        if self.age == CatAges.adult:
            self.protein_grams_needed[ProteinNeeds.dry_mass] =\
                self.protein_grams_needed[ProteinNeeds.dry_mass][self.activity]
        self.protein_grams_needed[ProteinNeeds.dry_mass] =\
            float(round(self.protein_grams_needed[ProteinNeeds.dry_mass], 2))
        return self.protein_grams_needed

    def determine_if_kitten(self) -> bool:
        """
        Sets a bool based on age compared against a list of kitten ages.

        Returns
        -------
        bool
        """
        self.is_kitten = False
        if self.age in kittens:
            self.is_kitten = True
        return self.is_kitten

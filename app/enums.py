from enum import Enum


class Range(Enum):
    min = "min"
    max = "max"
    avg = "avg"


class Nutrition(Enum):
    protein = "protein"
    fat = "fat"
    carbs = "carbs"
    moisture = "moisture"
    ash = "ash"
    fibre = "fibre"


class CatAges(Enum):
    kitten1 = 0
    kitten2 = 1
    kitten3 = 2
    adult = 3
    pregnant = 4
    mother = 5
    mother3 = 6


kittens = [CatAges.kitten1, CatAges.kitten2, CatAges.kitten3]


class CatActivities(Enum):
    indoor = 0
    outdoor = 1


class NumberNames(Enum):
    mer = "MER"
    der = "DER"
    protein_needs = Nutrition.protein


class NumberNamesLong(Enum):
    mer = "Maintenance Energy Requirement"
    der = "Daily Energy Requirement"


class ProteinNeeds(Enum):
    bodyweight = 1
    dry_mass = 2


class FoodType(Enum):
    dry = 0
    wet = 1

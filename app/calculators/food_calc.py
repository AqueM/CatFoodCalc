from app.enums import FoodType, Nutrition
from app.reference_data.food_values import gross_energy_values

protein = Nutrition.protein.value
fat = Nutrition.fat.value
fibre = Nutrition.fibre.value
ash = Nutrition.ash.value
moisture = Nutrition.moisture.value
carbs = Nutrition.carbs.value
mass = 'mass'

has_energy = [protein, fat, fibre]  # as per referenced sources, carbohydrates aren't counted in digestible energy


class Food:
    def __init__(self, **kwargs):
        self.percentages = {protein: float(kwargs[protein]),
                            fat: float(kwargs[fat]),
                            fibre: float(kwargs[fibre]),
                            ash: float(kwargs[ash]),
                            moisture: float(kwargs.get(moisture, 0)),
                            carbs: 0}
        self.mass = int(kwargs.get(mass, 0))

        self.food_type = self.get_food_type()
        self.percentages[carbs] = self.calculate_carbs()

        self.kcal_100g = self.calculate_digestible_energy_per_100g()
        self.percentage_dry_mass = self.calculate_dm_percentage()
        self.protein_100g_dry_mass = self.calculate_protein_in_100g_dm()
        self.kcal_package = self.calculate_energy_whole_package()

    def calculate_carbs(self) -> float:
        """
        Calculates and sets carbohydrate %
        by working out how much % is left after totaling other ingredient percentages

        Returns
        -------
        float
        """
        self.percentages[carbs] = round(100 - sum(value for key, value in self.percentages.items() if key != carbs), 2)
        if self.percentages[carbs] < 0:
            self.percentages[carbs] = 0
        return self.percentages[carbs]

    def calculate_kcal_gross_per_100g(self) -> float:
        """
        Calculates total energy in kcal based on
        the percentages of digested analytical ingredients (fat, protein, carbs, fibre) and their kcal per gram

        Gross energy calculations as per
        FEDIAF Nutritional Guidelines (2022), as detailed in
        Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
        7.2.2.1. Gross energy, Table VII-5.
        Predicted gross energy values of protein, fat and carbohydrate
        https://europeanpetfood.org/self-regulation/nutritional-guidelines/

        Returns
        -------
        float
        """
        gross_energy = 0
        for food_item in has_energy:
            gross_energy += self.percentages[food_item] * gross_energy_values[food_item]
        return round(gross_energy, 2)

    def get_food_type(self) -> FoodType:
        """
        Sets FoodType based on moisture %

        Returns
        -------
        FoodType
        """
        self.food_type = FoodType.wet
        if self.percentages[moisture] < 10:
            self.food_type = FoodType.dry
        return self.food_type

    def calculate_digestible_energy_per_100g(self) -> float:
        """
        Calculates and sets kcal amount per 100g for self.
        -------
        Formulas and numbers for digestible energy calculation come from
        FEDIAF Nutritional Guidelines(2022),
        as detailed in
        Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
        7.2.2.2. Metabolisable energy
        https://europeanpetfood.org/self-regulation/nutritional-guidelines/

        Returns
        -------        
        float
        """
        gross_energy = self.calculate_kcal_gross_per_100g()

        fibre_dry_mass_perc = \
            (self.percentages[fibre] * self.percentages[moisture]) / 100

        digestibility_modif = 87.9 - (0.88 * fibre_dry_mass_perc)  # as per cited paper
        digestible_energy = (gross_energy * digestibility_modif) / 100
        metabolic_energy_per_100 = digestible_energy - (0.77 * self.percentages[protein])  # as per cited paper
        self.kcal_100g = round(metabolic_energy_per_100, 2)
        return self.kcal_100g

    def calculate_energy_whole_package(self) -> None | float:
        """
        Calculates and sets kcal amount per package based on kcal per 100g and total package mass

        Returns
        -------
        float if mass is non-zero
        None is mass is > 0

        """
        if self.mass > 0:
            return self.kcal_100g * self.mass / 100
        else:
            return None

    def calculate_dm_percentage(self) -> float:
        """
        Calculates and sets % of dry mass based on moisture %

        Returns
        -------
        float
        """
        self.percentage_dry_mass = 100 - self.percentages[moisture]
        return self.percentage_dry_mass

    def calculate_protein_in_100g_dm(self) -> float:
        """
        Calculates and sets % of protein in dry mass based on total protein % and dry mass %

        Returns
        -------
        float
        """
        self.protein_100g_dry_mass = round((100 * self.percentages[protein]) / self.percentage_dry_mass, 0)
        return self.protein_100g_dry_mass

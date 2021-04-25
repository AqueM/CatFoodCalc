import statistics

# Protein requirements per kg cat body weight for adult cats as per
# NRC guidelines (2006) as detailed in
# https://www.msdvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-and-related-diseases-of-small-animals
# https://www.nap.edu/catalog/10668/nutrient-requirements-of-dogs-and-cats
# Assuming fully digestible protein source
from flaskr.enums import CatAges, Range, CatActivities

protein_needs_bodyweight = {
    CatAges.kitten1: 9,
    CatAges.kitten2: 9,
    CatAges.kitten3: 9,
    CatAges.adult: 5,
    CatAges.pregnant: 9,
    CatAges.mother: 9,
    CatAges.mother3: 9,
}

# Nutritional requirements per 100g of dry mass as per
# FEDIAF Nutritional Guidelines (2019), as detailed in
# Nutritional Guidelines For Complete and Complementary Pet Food for Cats and Dogs,
# section 3.2. Tables with nutrient recommendations, subsection 3.2.3.
# Recommended nutrient levels for cats TABLE III-4
# http://www.fediaf.org/images/FEDIAF_Nutritional_Guidelines_2019_Update_030519.pdf
# and
# as per AAFCO guidelines (2014) as detailed in
# AAFCO Methods For Substantiating Nutritional Adequacy Of Dog And Cat Foods
# https://www.aafco.org/Portals/0/SiteContent/Regulatory/Committees/Pet-Food/Reports/Pet_Food_Report_2013_Midyear-Proposed_Revisions_to_AAFCO_Nutrient_Profiles.pdf
# For foods with 4kcal/g calorie density

adult_protein_needs_dry_mass = {CatActivities.indoor: 25,
                                CatActivities.outdoor: 33}
kitten_protein_needs_dry_mass = 28
reproduction_protein_needs_dry_mass = 30

protein_needs_dry_mass_by_age = {
    CatAges.kitten1: kitten_protein_needs_dry_mass,
    CatAges.kitten2: kitten_protein_needs_dry_mass,
    CatAges.kitten3: kitten_protein_needs_dry_mass,
    CatAges.adult: adult_protein_needs_dry_mass,
    CatAges.pregnant: reproduction_protein_needs_dry_mass,
    CatAges.mother: reproduction_protein_needs_dry_mass,
    CatAges.mother3: reproduction_protein_needs_dry_mass,
}

fat_needs_dry_mass = {Range.min: 20,
                      Range.max: 50}

carbs_needs_dry_mass = {Range.min: 5,
                        Range.max: 10}


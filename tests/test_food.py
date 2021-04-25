# class TestFoodCalculations(unittest.TestCase):
#     test_cats_data = {
#         "cat1": [4, CatAges.adult, CatActivities.indoor],
#         "cat2": [6, CatAges.pregnant, CatActivities.outdoor],
#         "cat3": [2, CatAges.kitten1, CatActivities.outdoor]
#     }
#     test_cats_results = {
#         "cat1": {NumberNames.mer: {Range.min: 139.36, Range.max: 201},
#                  NumberNames.der: {Range.min: 139.36, Range.max: 201},
#                  NumberNames.protein_needs:
#                      {ProteinNeeds.bodyweight: 20,
#                       ProteinNeeds.dry_mass: 25}},
#         "cat2": {NumberNames.mer: {Range.min: 402, Range.max: 402},
#                  NumberNames.der: {Range.min: 562.8, Range.max: 562.8},
#                  NumberNames.protein_needs:
#                      {ProteinNeeds.bodyweight: 54,
#                       ProteinNeeds.dry_mass: 30}},
#         "cat3": {NumberNames.mer: {Range.min: 134, Range.max: 134}, NumberNames.der: {Range.min: 268, Range.max: 335},
#                  NumberNames.protein_needs:
#                      {ProteinNeeds.bodyweight: 18,
#                       ProteinNeeds.dry_mass: 28}},
#     }
#
#     methods_to_test = {NumberNames.der: "calculate_der",
#                        NumberNames.mer: "calculate_mer",
#                        NumberNames.protein_needs: "calculate_protein_needs"}
#

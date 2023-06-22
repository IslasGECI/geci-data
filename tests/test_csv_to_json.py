from geci_data import csv_to_dict


def test_csv_to_dict():
    csv_path = "tests/data/join_fenology_meals_result_and_peak_mass_per_nest.csv"
    csv_to_dict(csv_path)

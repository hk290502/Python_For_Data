import os

def get_contents_of_file(continent_name):
    base_path = os.path.dirname(__file__)
    filename = f"{continent_name}.csv"
    full_path = os.path.join(base_path, filename)

    if os.path.exists(full_path):
        with open(full_path, "r") as file:
            lines = file.readlines()
            return lines
    else:
        return None

def get_country_dict(country_list):
    countries_dict = {}
    if country_list:
        for line in country_list:
            clean_line = line.strip()
            if "," in clean_line:
                parts = clean_line.split(",")
            elif ";" in clean_line:
                parts = clean_line.split(";")
            else:
                continue

            if len(parts) == 2:
                country, capital = parts
                if country.lower() != "country":
                    countries_dict[country] = capital
    return countries_dict

def print_results(continent_name, countries):
    if countries:
        print(f"Countries in {continent_name}")
        print("-" * 40)
        for country, capital in countries.items():
            print(f"{country} has capital city {capital}")
        print(f"\nTotal countries: {len(countries)}")
    else:
        print(f"No data found for {continent_name}.")


continent_name = "Africa"



country_list = get_contents_of_file(continent_name)
print(f"country_list is: {country_list}")  # add this


countries = get_country_dict(country_list)


# list them out
print_results(continent_name, countries)
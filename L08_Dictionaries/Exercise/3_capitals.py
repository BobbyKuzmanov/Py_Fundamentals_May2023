country_names = input().split(", ")
capital_names = input().split(", ")
countries_capitals = dict(zip(country_names, capital_names))

for country, capital in countries_capitals.items():
    print(f"{country} -> {capital}")

# countries = input().split(", ")
# capitals = input().split(", ")
#
# capitals_by_country = {}
# for idx in range(len(countries)):
#     country  = countries[idx]
#     capital = capitals[idx]
#     capitals_by_country[country] = capital
#     print(f"{country} -> {capital}")


# Using a dictionary comprehension, write a program that receives country names on the first line, separated by
# comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and
# space ", "). Print each country with their capital on a separate line in the following format: "{country} ->
# {capital}".
#
# Input:
# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London
#
# Output:
# Bulgaria -> Sofia
# Romania -> Bucharest
# Germany -> Berlin
# England -> London
#
# Input:
# Bulgaria, Germany, France
# Varna, Frankfurt, Paris
#
# Output:
# Bulgaria -> Varna
# Germany -> Frankfurt
# France -> Paris

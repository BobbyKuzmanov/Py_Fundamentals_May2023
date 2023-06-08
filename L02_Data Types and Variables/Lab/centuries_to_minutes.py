centuries = int(input())
days_in_one_year = 365.2422
years = 100 * centuries
days = int(years * days_in_one_year)
hours = 24 * days
minutes = 60 * hours

print(f"{centuries} centuries = {years} "
      f"years = {days} days = {hours} hours = {minutes} minutes")

# Description ### Centuries to minutes ###
# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
# Assume that one year has 365.2422 days on average
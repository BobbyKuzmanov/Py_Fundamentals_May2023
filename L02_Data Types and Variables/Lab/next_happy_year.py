year = int(input())

while True:
    year += 1
    str_year = str(year)
    if len(str_year) == len(set(str_year)):#  'set'check and remove dublication
        print(year)
        break

# Description ## Next Happy Year ##
# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
import  re

date = input()
pattern = r"(?P<day>\d{2})(?P<separator>[-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
matches = re.finditer(pattern, date)
for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")

# Task:
# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing
# groups in your regular expression.
# Compose the Regular Expression
# Every valid date has the following characteristics:
#     • It always starts with two digits, followed by a separator
#     • After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
#     • After that, it has a separator and exactly 4 digits (for the year).
#     • The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
#     • The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a
# group backreference to check for this.
# You can follow the table below to help with composing your RegEx:
# Match all of these:
#     13/Jul/1928, 10-Nov-1934, 25.Dec.1937
# But not this:
#     1/Jan-1951, 23/sept/1973, 1/Feb/2016
#
# Input:
#     13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
# Output:
#     Day: 13, Month: Jul, Year: 1928
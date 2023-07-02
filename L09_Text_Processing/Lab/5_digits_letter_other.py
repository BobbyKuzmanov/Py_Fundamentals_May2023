text = input()
digits = ""
letters = ""
other = ""

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(digits)
print(letters)
print(other)

# Write a program that receives a single string.
# On the first line,
# print all the digits found in the string, on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter, and one other character.
#
# Input:
# Agd#53Dfg^&4F53
#
# Output:
# 53453
# AgdDfgF
# #^&
people_phone_numbers = {}
while True:
    command = input()
    if command.isdigit():
        break
    name, number = command.split('-')
    people_phone_numbers[name] = number

for _ in range(int(command)):
    name = input()
    if name in people_phone_numbers:
        print(f'{name} -> {people_phone_numbers[name]}')
    else:
        print(f'Contact {name} does not exist.')

# phonebook = {}
# n = 0
# while True:
#     line = input()
#     parts = line.split('-')
#     if len(parts) == 1:
#         n = int(line)
#         break
#     name = parts[0]
#     number = parts[1]
#     phonebook[name] = number
#
# for _ in range(n):
#     name = input()
#     if name in phonebook:
#         print(f'{name} -> {phonebook[name]}')
#     else:
#         print(f'Contact {name} does not exist.')

# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact
# by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print:
# "Contact {name} does not exist."
#
# Input:
# Adam-0888080808
# 2
# Mery
# Adam
#
# Output:
# Contact Mery does not exist.
# Adam -> 0888080808
#
# Input:
# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf
#
# Output:
# Silvester -> 02/987665544
# Contact silvester does not exist.
# Contact Rolf does not exist.
# Ralf -> 666

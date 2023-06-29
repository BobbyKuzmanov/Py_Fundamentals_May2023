elements = input().split()
bakery = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

print(bakery)

# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single
# space (the first element is the key, the second – the value, and so on). Create a dictionary with all the keys and
# values and print it on the console.
#
# Input:
# bread 10 butter 4 sugar 9 jam 12
# Output:
# {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
#
# Input:
# eggs 3 sugar 7 salt 1 butter 3
# Output:
# {'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}

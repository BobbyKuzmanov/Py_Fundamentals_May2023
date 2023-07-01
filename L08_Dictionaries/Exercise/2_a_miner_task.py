sequence_string = input()
dictionary = {}
while sequence_string != "stop":
    quantity = int(input())
    if sequence_string not in dictionary:
        dictionary[sequence_string] = 0
    dictionary[sequence_string] += quantity
    sequence_string = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")

# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].
#
# Input:
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop
#
# Output:
# Gold -> 155
# Silver -> 10
# Copper -> 17

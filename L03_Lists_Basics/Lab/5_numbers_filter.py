number_of_lines = int(input())
numbers = []
filtered = []

for i in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)
    
command = input()
if command == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
if command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
if command == 'positive':
    for number in numbers:
        if number >= 0:
            filtered.append(number)
if command == 'negative':
    for number in numbers:
        if number < 0:
            filtered.append(number)
print(filtered)

# n = int(input())

# constant values
# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_NEGATIVE = 'negative'
# COMMAND_POSITIVE = 'positive'

# accepting numbers from user
# numbers = [int(input()) for _ in range(n)]
#
# filtered_numbers = []
#
# # for _ in range(n):
# #     number = int(input())
# #     numbers.append(number)
#
# command = input()
#
# for num in numbers:
#     filter_command = (
#         (command == COMMAND_EVEN and num % 2 == 0) or
#         (command == COMMAND_ODD and num % 2 != 0) or
#         (command == COMMAND_POSITIVE and num >= 0) or
#         (command == COMMAND_NEGATIVE and num < 0)
#     )
#
#     if filter_command:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)

# Description #
# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# • even
# • odd
# • negative
# • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even).
# Finally, print the result.

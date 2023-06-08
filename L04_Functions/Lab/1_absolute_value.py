numbers_list = input().split()

absolute_values = []

for num in numbers_list:
    absolute_values.append(abs(float(num)))

print(absolute_values)

# Description #
# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value
# as a list. Use abs()

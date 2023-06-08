def round_numbers(numbers):
    rounded_numbers = []
    for num in numbers:
        rounded_numbers.append(round(float(num)))
    return rounded_numbers


my_list = input().split()
rounded_numbers = round_numbers(my_list)
print(rounded_numbers)

# Description #
# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

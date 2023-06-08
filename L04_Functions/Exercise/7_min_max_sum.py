def find_min_max_sum(numbers):
    numbers_list = []
    for num in numbers.split():
        numbers_list.append(int(num))

    minimum = min(numbers_list)
    maximum = max(numbers_list)

    total_sum = 0
    for num in numbers_list:
        total_sum += num

    print("The minimum number is", minimum)
    print("The maximum number is", maximum)
    print("The sum number is:", total_sum)


input_numbers = input()
find_min_max_sum(input_numbers)

# Description #
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
# • On the first line: "The minimum number is {minimum number}"
# • On the second line: "The maximum number is {maximum number}"
# • On the third line: "The sum number is: {sum of all numbers}"
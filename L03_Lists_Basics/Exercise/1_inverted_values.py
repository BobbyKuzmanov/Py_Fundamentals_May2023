numbers_list = input().split()  # split the input string into individual numbers using the split()
opposite_nums = []

for current in numbers_list:
    opposite_nums.append(-int(current))  # convert it to an integer using the int()
    # function and then negate it using the unary minus operator - .
print(opposite_nums)

# Description #
# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

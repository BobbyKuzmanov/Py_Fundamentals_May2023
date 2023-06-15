numbers = input().split()
numbers = list(map(int, numbers))

average = sum(numbers) / len(numbers)
greater_numbers = [num for num in numbers if num > average]

if len(greater_numbers) == 0:
    print("No")
else:
    top_numbers = sorted(greater_numbers, reverse=True)[:5]
    print(*top_numbers)

# numbers = list(map(int, input().split()))
#
# average = sum(numbers) / len(numbers)
# greater_numbers = []
#
# for num in numbers:
#     if num > average:
#         greater_numbers.append(num)
#
# if not greater_numbers:
#     print("No")
# else:
#     top_numbers = sorted(greater_numbers, reverse=True)[:5]
#     print(*top_numbers)

# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average
# value in the sequence, sorted in descending order.
# Input
# • Read from the console a single line holding space-separated integers.
# Output
# • Print the above-described numbers on a single line, space-separated.
# • If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# • Print "No" if no numbers hold the above property.
# Constraints
# • All input numbers are integers in the range [-1 000 000 … 1 000 000].
# • The count of numbers is in the range [1…10 000].

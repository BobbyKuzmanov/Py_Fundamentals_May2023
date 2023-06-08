def is_palindrome(some_digit):
    if some_digit == some_digit[::-1]:
        return True
    return False


# Take input from the user
num = input().split(', ')

# Check if the number is a palindrome or not
for current in num:
    print(is_palindrome(current))

# Description #
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.
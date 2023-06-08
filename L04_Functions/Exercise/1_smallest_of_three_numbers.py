def smallest_number(some_number):
    min_element = min(some_number)
    return min_element


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
result = smallest_number(numbers)
print(result)

# Description #
# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use
# an appropriate name for the function

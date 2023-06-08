def calc_factorial(number):
    for current in range(1,number):
        number *= current
    return number


first_number = int(input())
second_number = int(input())
result = calc_factorial(first_number) / calc_factorial(second_number)
print(f'{result:.2f}')

# Description #
# Write a function that receives two integer numbers.
# Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
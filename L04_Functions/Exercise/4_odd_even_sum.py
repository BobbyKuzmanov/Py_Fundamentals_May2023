def sum_odd_even(somenumber):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for current in somenumber:
        if int(current) % 2 == 0:
            sum_of_even_digits += int(current)
        else:
            sum_of_odd_digits += int(current)

    return sum_of_odd_digits, sum_of_even_digits


number = input()
odd_digits, even_digits = sum_odd_even(number)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")

# Description #
# You will receive a single number.
# You should write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

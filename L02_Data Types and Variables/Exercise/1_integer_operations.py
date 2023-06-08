first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())

addition_first_second = first_number + second_number
divide = int(addition_first_second / third_number)
multiplication = divide * fourth_number

print(f'{multiplication:.0f}')

# Description ### Integer operations ###
# Write a program that reads four integer numbers.
# It should add the first to the second number, integer divide the
# sum by the third number, and multiply the result by the fourth number.
# Print the final result.
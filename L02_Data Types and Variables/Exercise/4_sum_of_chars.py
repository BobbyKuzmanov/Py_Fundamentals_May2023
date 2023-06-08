number = int(input())
sum_of_codes = 0

for i in range(number):
    char = input()
    code_in_ascii = ord(char)
    sum_of_codes += code_in_ascii

print(f'The sum equals: {sum_of_codes}')

# Describtion ### Sum of chars ###
# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line,you will receive N – the number of lines.
# On the following N lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1...20].

letter_sequence = input()
result = ""
for i in range(len(letter_sequence)):
    if i == 0:
        result += letter_sequence[i]
    elif letter_sequence[i] != letter_sequence[i-1]:
        result += letter_sequence[i]

print(result)

# Write a program that reads a string from the console and replaces any sequence
# of the same letters with a single corresponding letter.
#
# Input:
#     aaaaabbbbbcdddeeeedssaa
#
# Output
#     abcdedsa

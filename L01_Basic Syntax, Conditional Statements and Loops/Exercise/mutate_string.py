first_string = input()
second_string = input()

last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1] # [0:character_index + 1:1]
    right_part = first_string[character_index + 1:] # [character_index + 1:len(first_string):1]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
#####   Task Description   ##### 10. * Mutate Strings
# You will be given two strings.
# Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
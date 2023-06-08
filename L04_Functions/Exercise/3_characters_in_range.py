def characters(a, b):
    for current in range(ord(a) + 1, ord(b)):
        print(chr(current), end='')


first_char = input()
second_char = input()
characters(first_char, second_char)

# Description #
# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

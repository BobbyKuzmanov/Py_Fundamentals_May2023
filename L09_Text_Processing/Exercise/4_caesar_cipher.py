sentence = input()

for char in sentence:
    print(chr(ord(char) + 3), end="")

# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.
#
# Input:
# Programming is cool!
#
# Output:
# Surjudpplqj#lv#frro$

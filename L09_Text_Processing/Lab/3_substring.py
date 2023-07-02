word_one = input()
word_two = input()

while word_one in word_two:
    word_two = word_two.replace(word_one, "")

print(word_two)

# On the first line, you will receive a string. On the second line, you will receive a second string.
# Write a program that removes all the occurrences of the first string in the second until there is no match.
# At the end, print the remaining string.
#
# Input:
# ice
# kicegiciceeb
#
# Output:
# kgb
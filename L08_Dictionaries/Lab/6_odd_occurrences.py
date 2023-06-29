words = input().split()
words_dict = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in words_dict:
        words_dict[word_lower] = 0
    words_dict[word_lower] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")


# Write a program that prints all elements from a given sequence of words that occur an odd number of times
# (case-insensitive) in it.
#     • Words are given on a single line, space-separated.
#     • Print the result elements in lowercase, in their order of appearance.
#
# Input:
# Java C# PHP PHP JAVA C java
# Output:
# java c# c
#
# Input:
# 3 5 5 hi pi HO Hi 5 ho 3 hi pi
# Output:
# 5 hi
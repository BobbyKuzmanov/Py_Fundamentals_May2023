words = input().split()
for word in words:
    print(word * len(word), end="")
# Write a program that reads a sequence of strings, separated by a single space.
# Each string should be repeated N times, where N is the length of the string.
# Print the final strings concatenated into one string.
#
# Input:
# hi abc add
#
# Output:
# hihiabcabcabcaddaddadd
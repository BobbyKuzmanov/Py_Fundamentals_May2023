words = input().split()
count_by_char = {}

for word in words:
    for letter in word:
        if letter in count_by_char:
            count_by_char[letter] += 1
        else:
            count_by_char[letter] = 1

for letter, count in count_by_char.items():
        print(f"{letter} -> {count}")


# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

# Input:
# text
# Output:
# t -> 2
# e -> 1
# x -> 1

some_string = input()
strength = 0
result = ""
for i in range(len(some_string)):
    if some_string[i] == ">":
        strength += int(some_string[i + 1])
        result += ">"
    elif some_string[i] != ">" and strength > 0:
        strength -= 1
    else:
        result += some_string[i]

print(result)

# Write a program that reads a string from the console that contains:
#     • Explosions marked with '>'
#     • Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
#     • Any other characters
# Your task is to delete x characters, starting after the exploded character ('>').
# If you find another explosion mark ('>') while deleting characters,
# you should add the strength to your previous explosion.
# You should not delete the explosion character – '>'.
#
# Input:
#     abv>1>1>2>2asdasd
#
# Output:
#     abv>>>>dasd

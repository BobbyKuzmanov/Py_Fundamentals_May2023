text = input()
while text != "end":
    print(f"{text} = {text[::-1]}")
    text = input()


# You will be given strings on separate lines until you receive an "end" command.
# Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".
#
# Input:
# helLo
# Softuni
# bottle
# end
#
# Output:
# helLo = ollHe
# Softuni = uninufS
# bottle = elbottle

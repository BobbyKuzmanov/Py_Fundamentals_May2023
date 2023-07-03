text = input()
for i in range(len(text)):
    if text[i] == ":":
        print(f":{text[i + 1]}")

# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
#
# Input:
#  There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
#
# Output:
# :P
# :O
# :)
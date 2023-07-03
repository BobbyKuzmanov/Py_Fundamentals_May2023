text = input().split()
result = 0
for i in range(min(len(text[0]), len(text[1]))):
    result += ord(text[0][i]) * ord(text[1][i])

if len(text[0]) > len(text[1]):
    for i in range(len(text[1]), len(text[0])):
        result += ord(text[0][i])

if len(text[0]) < len(text[1]):
    for i in range(len(text[0]), len(text[1])):
        result += ord(text[1][i])

print(result)
# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows:
# multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.
#
# Input:
# George Peter
#
# Output:
# # 52114
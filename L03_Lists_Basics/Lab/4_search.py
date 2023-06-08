number = int(input())
word = input()

string = []

for current_string in range(number):
    currurent_string = input()
    string.append(currurent_string)
print(string)

for i in range(len(string) - 1, -1, -1):
    element = string[i]
    if word not in element:
        string.remove(element)
print(string)

# Description #
# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines,you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.
